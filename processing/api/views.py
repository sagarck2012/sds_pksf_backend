import sys
import json
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import CreateAPIView
from .serializer import HarvestSearchSerializer, PackagingSerializer
from .serializer import *
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .raw_sql_query import *
from django.db import connection
from django.core.serializers.json import DjangoJSONEncoder
import json
from rest_framework import status
from processing.models import *
from datetime import date, datetime
from django.utils.crypto import get_random_string
from random import randint
from django.db import transaction
# from datetime import timedelta
from users.decorators import access_permission_required
# import logging
# logger = logging.getLogger('django')
from processing.api.serializer import CrateRegisterSerializer
from processing.models import CrateInfo, PackagingDetail, Crating, CratingDetail
from processing.utils import get_crate_code, generate_crating_code, generate_shipping_code
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from farming.models import Land, Seeding, Plot, Harvesting
from users.models import User
from django.db.models import Sum

def get_all(cursor):
    """
    Return all rows from a cursor as a dict
    """
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class HarvestSearchAPIView(APIView):
    @swagger_auto_schema(request_body=HarvestSearchSerializer)
    @access_permission_required
    def post(self, request):
        # print(request.data)
        start_date = request.data['start_date']
        end_date = request.data['end_date']
        crop_type_id = request.data['crop_type_id']

        query = get_harvest_for_packaging(start_date+" 00:00:00", end_date + " 23:59:59", crop_type_id)
        # print(query)

        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                # get_all method return List
                # json.dumps convert it to string; here cls=DjangoJsonEncoder is used to  resolve 'date-object' is not json
                # serializable issue of std. python library
                # json.loads convert it to json object
                query_data = json.loads(json.dumps(get_all(cursor), cls=DjangoJSONEncoder))
                # print(f"query data: {query_data} & type {type(query_data)}")
                # print(f"start date: {start_date}, end date: {end_date}, crop id : {crop_id}")
                return Response({"success": True,
                                 "harvest_list": query_data,
                                 "status_code": status.HTTP_200_OK
                                 }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            # logger.warning("something went wrong")
            return Response({"success": False,
                             "message": "Error! Please try again",
                             "status_code": status.HTTP_400_BAD_REQUEST
                             }, status=status.HTTP_400_BAD_REQUEST)


class PackagingAddAPIView(APIView):
    @swagger_auto_schema(request_body=PackagingSerializer)
    @access_permission_required
    def post(self, request):
        # print(request.data)
        # get harvest_id_list to update harvest row status
        # get latest_harvest_id for qr_code url
        print(f"harvest_id_list: {request.data['harvest_id_list']} & type : {type(request.data['harvest_id_list'])}")
        try:
            harvest_id_list = json.loads(request.data['harvest_id_list'])  # convert str to list & sort ASC
            print(f"harvest_id_list: {harvest_id_list} & type: {type(harvest_id_list)}")
            latest_harvest_id = sorted(harvest_id_list)[-1]  # sort list in ASC order and get latest harvest id
        except Exception as e:
            print(e)
            return Response({"success": False,
                             "message": "Error! Invalid harvest list format; Send harvest ids like '[1,2,3]'",
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)

        # check harvest id validity and get crop id, crop_type_id
        valid_harvest_id, crop_id, crop_type_id = check_harvest_id_validity(latest_harvest_id)
        if valid_harvest_id is True:
            qr_code = "url/" + str(latest_harvest_id) + "/"
        else:
            return Response({"success": False,
                             "message": "Invalid harvest id",
                             "status_code": status.HTTP_400_BAD_REQUEST
                             },
                            status=status.HTTP_400_BAD_REQUEST)

        # generate unique processing_id and update corresponding harvest rows
        processing_id = generate_processing_id()

        with transaction.atomic():
            update_harvest_rows(processing_id, harvest_id_list)
            # removing keys for crating proper model serializer instance
            user_id = request.data['user_id']
            del request.data['harvest_id_list']
            del request.data['user_id']
            serializer = PackagingSerializer(data=request.data)
            if serializer.is_valid():
                # get total quantity
                quantity_in_float = Harvesting.objects.filter(id__in=harvest_id_list).aggregate(Sum('quantity'))
                # convert it to integer
                quantity_in_int = int(quantity_in_float['quantity__sum'])
                packaging_unit_per_package = int(request.data['packaging_unit_per_package'])

                # if quantity_in_int % packaging_unit_per_package != 0:
                #     return Response({"success": False,
                #                      "message": 'selected quantity must be divisible by packaging_unit_per_package',
                #                      "status_code": status.HTTP_400_BAD_REQUEST},
                #                     status=status.HTTP_400_BAD_REQUEST)
                # else:
                    #  calculate total no of sticker
                    # total_no_of_sticker = quantity_in_int//packaging_unit_per_package

                package_data = serializer.save(processing_id=processing_id,
                                               created_by=user_id,
                                               last_updated_by=user_id,
                                               crop_id=crop_id,
                                               crop_type_id=crop_type_id,
                                               quantity=quantity_in_int
                                               )
                # INSERT INTO sticker table
                insert_data_to_packaging_detail(package_data, qr_code)
                return Response({"success": True,
                                 "message": 'Sticker generated successfully',
                                 "status_code": status.HTTP_201_CREATED},
                                status=status.HTTP_201_CREATED)
            else:
                return Response({"success": False,
                                 "message": f'Error {serializer.errors}',
                                 "status_code": status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)


# class CropListAPIView(APIView):
#
#     def get(self, request):
#         crop = Crop.objects.filter(delete_status=0)  # only active crop
#         serializer = CropSerializer(crop, many=True)
#         print(f'serializer: {serializer}')
#         return Response(serializer.data)


class CrateRegisterAPIView(CreateAPIView):
    serializer_class = CrateRegisterSerializer

    def post(self, request, **kwargs):
        if 'user_id' not in request.data.keys() or request.data['user_id'] is '':
            raise ValidationError({'success': False, 'message': 'user_id is required', 'status_code': status.HTTP_400_BAD_REQUEST})
        if 'production_house' not in request.data.keys() or request.data['production_house'] is '':
            raise ValidationError({'success': False, 'message': 'production_house is required', 'status_code': status.HTTP_400_BAD_REQUEST})

        user_id = request.data['user_id']
        production_house = request.data['production_house']
        crate_no, bar_code = get_crate_code(user_id)  # generate crate_no, bar_code
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(crate_no=crate_no, bar_code=bar_code, production_house_id=production_house, created_by=user_id)

        response = {
            'success': True,
            'status_code': status.HTTP_201_CREATED,
            'message': 'crate registered  successfully!',
            'crate_no': crate_no,
            'bar_code': bar_code
        }

        return Response(response, status=status.HTTP_201_CREATED)


class ReadyCrateListAPIView(CreateAPIView):
    serializer_class = CrateRegisterSerializer

    def post(self, request, **kwargs):
        if 'user_id' not in request.data.keys() or request.data['user_id'] is '':
            raise ValidationError({'success': False, 'message': 'user_id is required', 'status_code': status.HTTP_400_BAD_REQUEST})
        try:
            user = User.objects.get(id=request.data['user_id'])
            crate_info = CrateInfo.objects.filter(status='ready', production_house=user.production_house, delete_status=0).order_by('-pk')
            serializer = self.serializer_class(crate_info, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ObjectDoesNotExist:
            return Response({'message': 'user_id not found', 'success': False}, status=status.HTTP_400_BAD_REQUEST)

# ReadyCrateListAPIView :
# filter by status = ready ; production_house of {{ request.data['user_id'] }}


class CrateEditAPIView(APIView):

    def put(self, request):
        if 'user_id' not in request.data.keys() or request.data['user_id'] is '':
            raise ValidationError({'message': 'user_id is required', 'status_code': status.HTTP_400_BAD_REQUEST})
        if 'crate_id' not in request.data.keys() or request.data['crate_id'] is '':
            raise ValidationError({'message': 'crate_id is required', 'status_code': status.HTTP_400_BAD_REQUEST})

        try:
            user_id = request.data['user_id']
            crate = CrateInfo.objects.get(id=request.data['crate_id'], delete_status=0)
            serializer = CrateRegisterSerializer(crate, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(last_updated_by=user_id)
            return Response({'message': 'crate updated!', 'success': True}, status=status.HTTP_202_ACCEPTED)

        except ObjectDoesNotExist:
            return Response({'message': 'crate_id not found', 'success': False}, status=status.HTTP_400_BAD_REQUEST)


class CrateDeleteAPIView(DestroyAPIView):

    def delete(self, request):
        if 'user_id' not in request.data.keys() or request.data['user_id'] is '':
            raise ValidationError({'message': 'user_id is required', 'status_code': status.HTTP_400_BAD_REQUEST})
        if 'crate_id' not in request.data.keys() or request.data['crate_id'] is '':
            raise ValidationError({'message': 'crate_id is required', 'status_code': status.HTTP_400_BAD_REQUEST})

        try:
            user_id = request.data['user_id']
            crate = CrateInfo.objects.get(id=request.data['crate_id'], delete_status=0)
            crate.delete_status = 1
            crate.last_updated_by = user_id
            crate.save()
            return Response({'message': 'crate deleted!', 'success': True}, status=status.HTTP_202_ACCEPTED)

        except ObjectDoesNotExist:
            return Response({'message': 'crate_id not found', 'success': False}, status=status.HTTP_400_BAD_REQUEST)


# class CrateAddPackageAPIView(APIView):
#
#     def post(self, request, crate_bar_code=None, *args, **kwargs):
#         if 'user_id' not in request.data.keys() or request.data['user_id'] is '':
#             raise ValidationError({'message': 'user_id is required', 'status_code': status.HTTP_400_BAD_REQUEST})
#         if 'bar_code' not in request.data.keys() or request.data['bar_code'] is '':
#             raise ValidationError({'message': 'bar_code list is required', 'status_code': status.HTTP_400_BAD_REQUEST})
#         if 'crate_id' not in request.data.keys() or request.data['crate_id'] is '':
#             raise ValidationError({'message': 'crate_id is required', 'status_code': status.HTTP_400_BAD_REQUEST})
#
#         try:
#             user_id = request.data['user_id']
#             bar_code = list(request.data['bar_code'])
#             crate_id = request.data['crate_id']
#             # crate_code = CrateInfo.objects.get(bar_code=crate_bar_code, delete_status=0)
#             valid_package_id = []
#             invalid_bar_code = []
#
#             for i in bar_code:
#                 try:
#                     package = PackagingDetail.objects.get(sticker_bar_code=i, status='printed')
#                     valid_package_id.append(package.pk)
#                 except (ObjectDoesNotExist, PackagingDetail.MultipleObjectsReturned):
#                     invalid_bar_code.append(i)
#
#             # only for ALL valid bar_code -> tbl status change, entry
#             if len(valid_package_id) > 0:
#                 print(f"valid_packaging_id > {valid_package_id}")
#                 with transaction.atomic():
#                     # adding to crating master tbl
#                     crating_master = Crating.objects.create(crate_id=crate_id, total_no_of_package=len(valid_package_id), create_by=user_id, status='ready')
#                     print(f"crating master: {crating_master.id}")
#
#                     # adding to crating detail tbl
#                     for j in valid_package_id:
#                         CratingDetail.objects.create(process_packaging_detail_id=j, process_crating_master_id=crating_master.id, scanned_by=user_id, status='ready')
#
#                     # packaging detail table status change
#                     PackagingDetail.objects.filter(id__in=valid_package_id).update(status='crated')
#
#                     return Response({'message': 'package crated successfully!', 'success': True},
#                                 status=status.HTTP_201_CREATED)
#
#             # if ONE of the bar_code invalid -> dont proceed
#             else:
#                 print(f"invalid_bar_code > {invalid_bar_code}")
#                 return Response({'message': 'bar_code invalid!',
#                                  'success': False,
#                                  'invalid bar_code list': invalid_bar_code}, status=status.HTTP_400_BAD_REQUEST)
#
#         except Exception as e:
#             error = 'online {}'.format(sys.exc_info()[-1].tb_lineno), e
#             print(error)
#             return Response({'message': "failed!", 'success': False}, status=status.HTTP_400_BAD_REQUEST)


def insert_data_to_packaging_detail(package_data, qr_code):
    total_no_of_sticker = package_data.total_no_of_sticker
    print(f"no_of_sticker: {total_no_of_sticker} & processing_id: {package_data.pk}")

    for data in range(0, int(total_no_of_sticker)):
        PackagingDetail.objects.create(
            process_packaging_master_id=package_data.pk,
            processing_id=package_data.processing_id,
            sticker_qr_code=qr_code,
            sticker_bar_code=get_sticker_bar_code(),
            generated_by=package_data.created_by,
            generated_at=package_data.created_at,
            # Default: generated; damaged, crated, shipped, received
            status="generated"
        )


def check_harvest_id_validity(latest_harvest_id):
    # Check if harvest id is valid
    try:
        harvest = Harvesting.objects.get(pk=latest_harvest_id)
        crop_id = harvest.plot.crop_id
        crop_type_id = harvest.plot.crop_type_id
        if harvest.status == "partially harvested" or harvest.status == "fully harvested":
            return True, crop_id, crop_type_id
        else:
            return False, crop_id, crop_type_id
    except Exception as e:
        print(e)
        return False


def get_sticker_bar_code():
    today = date.today()
    d1 = today.strftime("%d%m%y")  # today in ddmmyy format
    random_num = str(randint(100000, 999999))
    bar_code = d1 + random_num
    # check for uniqueness
    if PackagingDetail.objects.filter(sticker_bar_code=bar_code).exists():
        get_sticker_bar_code()
    else:
        return bar_code


def generate_processing_id():
    today = date.today()
    d1 = today.strftime("%d%m%y")  # today in ddmmyy format
    random_str = get_random_string(6).upper()    # 6 random string using django.utils.crypto
    processing_id = d1 + random_str
    # check for uniqueness
    if Packaging.objects.filter(processing_id=processing_id).exists():
        generate_processing_id()
    else:
        return processing_id


def update_harvest_rows(processing_id, harvest_id_list):
    # print(f"processing_id: {processing_id} inside update harvest rows")
    # change harvest status to packaged
    for harvest_id in harvest_id_list:
        Harvesting.objects.filter(pk=harvest_id).update(processing_id=processing_id, status="packaged")


class PackagingSearchAPIView(APIView):
    @swagger_auto_schema(request_body=PackagingSearchSerializer)
    @access_permission_required
    def post(self, request):
        print(request.data)
        # start_date = request.data['start_date']
        # end_date = request.data['end_date']
        # crop_id = request.data['crop_id']
        crop_type_id = request.data['crop_type_id']

        # convert date string to date object for proper django orm query i.e. add 1 day to end
        # date if star date is equal to end date
        # start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
        # end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
        # if start_date_obj == end_date_obj:
        #     end_date_obj = end_date_obj + timedelta(days=1)
        # else:
        #     pass

        # query = get_created_packaging_list(start_date + " 00:00:00", end_date + " 23:59:59", crop_type_id)
        query = get_created_packaging_list(crop_type_id)
        print(query)

        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                # get_all method return List
                # json.dumps convert it to string; here cls=DjangoJsonEncoder is used to  resolve 'date-object' is not json
                # serializable issue of std. python library
                # json.loads convert it to json object
                query_data = json.loads(json.dumps(get_all(cursor), cls=DjangoJSONEncoder))
                # print(f"query data: {query_data} & type {type(query_data)}")
                # print(f"start date: {start_date}, end date: {end_date}, crop id : {crop_id}")
                return Response({"success": True,
                                 "package_list": query_data,
                                 "status_code": status.HTTP_200_OK},
                                status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"success": False,
                             "message": "Error! Please try again",
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)


class StickerSearchAPIView(APIView):
    @swagger_auto_schema(request_body=StickerSearchSerializer)
    @access_permission_required
    def post(self, request):
        print(request.data)
        processing_id = request.data['processing_id']
        query = get_sticker_of_package("%"+processing_id+"%")  # adding % for LIKE query
        print(query)
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                # get_all method return List
                # json.dumps convert it to string; here cls=DjangoJsonEncoder is used to  resolve 'date-object' is not json
                # serializable issue of std. python library
                # json.loads convert it to json object
                query_data = json.loads(json.dumps(get_all(cursor), cls=DjangoJSONEncoder))
                # print(f"query data: {query_data} & type {type(query_data)}")
                # print(f"start date: {start_date}, end date: {end_date}, crop id : {crop_id}")
                return Response({"success": True,
                                 "sticker_list": query_data,
                                 "status_code": status.HTTP_200_OK},
                                status=status.HTTP_200_OK
                                )
        except Exception as e:
            # print(e)
            return Response({"success": False,
                             "message": f'Error {e}',
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)


class StickerDamagedAPIView(APIView):
    @swagger_auto_schema(request_body=StickerDamagedSerializer)
    @access_permission_required
    def post(self, request):
        print(request.data)
        sticker_id = request.data['sticker_id']
        comment = request.data['comment']
        delete_by = request.data['user_id']
        # search the sticker in Packaging Detail Table and verify for validity
        try:
            sticker = PackagingDetail.objects.get(pk=sticker_id, status="printed")

        except PackagingDetail.DoesNotExist:
            return Response({"success": False,
                             "message": "Invalid sticker id! Please try again",
                             "status": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                # Update sticker status to damaged
                PackagingDetail.objects.filter(pk=sticker_id, status="printed").update(status="damaged",
                                                                                       comment=comment)
                # Create a row in PackagingDamaged Table
                PackagingDamaged.objects.create(
                    process_packaging_master_id=sticker.process_packaging_master_id,
                    processing_id=sticker.processing_id,
                    sticker_qr_code=sticker.sticker_qr_code,
                    sticker_bar_code=sticker.sticker_bar_code,
                    # reprinted_against = models.CharField(max_length=255, blank=True, null=True)
                    # manual_print = models.BooleanField(default=False)
                    process_crating_master_id=sticker.process_crating_master_id,
                    process_shipping_master_id=sticker.process_shipping_master_id,
                    process_receiving_master_id=sticker.process_receiving_master_id,
                    shipping_id=sticker.shipping_id,
                    deleted_by=delete_by,
                    deleted_at=datetime.now(),
                    # Default: damaged
                    status="damaged",
                    comment=sticker.comment

                )

                # Generate a new sticker for damaged sticker
                PackagingDetail.objects.create(
                    process_packaging_master_id=sticker.process_packaging_master_id,
                    processing_id=sticker.processing_id,
                    sticker_qr_code=sticker.sticker_qr_code,
                    sticker_bar_code=get_sticker_bar_code(),
                    generated_by=delete_by,
                    generated_at=datetime.now(),
                    # Default: generated; damaged, crated, shipped, received
                    status="generated"
                )

        except Exception as e:
            print(e)
            return Response({"success": False,
                             "message": f'Error {e}',
                             "status_code": status.HTTP_400_BAD_REQUEST
                             },
                            status=status.HTTP_400_BAD_REQUEST)

        # except Exception as e:
        #     print(e)
        #     return Response({"message": "Error in generating new sticker! Please try again"},
        #                     status=status.HTTP_400_BAD_REQUEST)

        return Response({"success": True,
                         "message": "Success!",
                         "status_code": status.HTTP_200_OK},
                        status=status.HTTP_200_OK)


class StickerPrintedAPIView(APIView):
    @swagger_auto_schema(request_body=StickerPrintedSerializer)
    @access_permission_required
    def post(self, request):

        try:
            sticker_id_list = json.loads(request.data['sticker_id_list'])  # convert str to list
        except Exception as e:
            print(e)
            return Response({"success": False,
                            "message": f'Error {e}\n Invalid sticker_id_list format. '
                                       f'Send sticker_id_list like [1,2,3] (list in a string)  ',
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            with transaction.atomic():
                for sticker in sticker_id_list:
                    PackagingDetail.objects.filter(pk=sticker, status="generated").update(status="printed")
                return Response({"success": True,
                                 "message": 'Sticker status updated successfully',
                                 "status_code": status.HTTP_200_OK},
                                status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"success": False,
                             "message": f'Error {e}',
                             "status":  status.HTTP_400_BAD_REQUEST
                             },
                            status=status.HTTP_400_BAD_REQUEST)


class StickerDetailAPIView(APIView):
    @swagger_auto_schema(request_body=StickerDetailSerializer)
    # @access_permission_required
    def post(self, request):
        print(request.data['harvest_id'])
        package_detail = {}
        try:
            # query for package_detail dictionary
            harvest_data = Harvesting.objects.get(pk=request.data['harvest_id'])  # get harvest data for production date
            harvest_processing_id = harvest_data.processing_id  # get processing_id for packaging master data
            plot_id = harvest_data.plot_id  # get plot_id for crop & crop type name
            packaging_data = Packaging.objects.get(processing_id=harvest_processing_id)
            plot_data = Plot.objects.get(pk=plot_id)
            seeding_data = Seeding.objects.get(pk=plot_data.seeding_id)
            land_data = Land.objects.get(pk=seeding_data.land_id)
            production_house_data = ProductionHouse.objects.get(pk=land_data.production_house.id)

            # populate package_detail dictionary
            package_detail['production_date'] = harvest_data.created_at
            package_detail['quality'] = "organic"
            package_detail['best_before'] = packaging_data.exp_date
            package_detail['net_weight'] = packaging_data.packaging_unit_per_package
            package_detail['packaging_unit'] = packaging_data.packaging_unit
            package_detail['production_house_name'] = production_house_data.name
            package_detail['production_house_address'] = production_house_data.address
            package_detail['production_house_contact'] = production_house_data.email
            package_detail['crop_name'] = plot_data.crop.name
            package_detail['crop_type_eng_name'] = plot_data.crop_type.eng_name
            package_detail['crop_type_local_name'] = packaging_data.crop_type.local_name

            return Response({"success": True,
                             "package_detail": package_detail,
                             "status_code": status.HTTP_200_OK},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"success": False,
                             "message": f'Error {e}',
                            "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)


class CratingAddAPIView(APIView):

    def post(self, request):
        if 'user_id' not in request.data.keys() or request.data['user_id'] is '':
            raise ValidationError({'message': 'user_id is required', 'status_code': status.HTTP_400_BAD_REQUEST})
        if 'bar_code' not in request.data.keys() or request.data['bar_code'] is '':
            raise ValidationError({'message': 'bar_code list is required', 'status_code': status.HTTP_400_BAD_REQUEST})
        if 'crate_id' not in request.data.keys() or request.data['crate_id'] is '':
            raise ValidationError({'message': 'crate_id is required', 'status_code': status.HTTP_400_BAD_REQUEST})

        try:
            user_id = request.data['user_id']
            bar_code = list(request.data['bar_code'])
            crate_id = request.data['crate_id']
            # crate_code = CrateInfo.objects.get(bar_code=crate_bar_code, delete_status=0)
            valid_package_id = []
            invalid_bar_code = []

            for i in bar_code:
                try:
                    package = PackagingDetail.objects.get(sticker_bar_code=i, status='printed')
                    valid_package_id.append(package.pk)
                except (ObjectDoesNotExist, PackagingDetail.MultipleObjectsReturned):
                    invalid_bar_code.append(i)

            # only for ALL valid bar_code -> tbl status change, entry
            if len(valid_package_id) > 0:
                print(f"valid_packaging_id > {valid_package_id}")
                crating_code = generate_crating_code()
                with transaction.atomic():

                    # updating crate_info tbl
                    CrateInfo.objects.filter(id=crate_id).update(status='crated')

                    # adding to crating master tbl
                    crating_master = Crating.objects.create(crate_id=crate_id, crating_code=crating_code,
                                                            total_no_of_package=len(valid_package_id),
                                                            create_by=user_id, status='crated')
                    print(f"crating master: {crating_master.id}")

                    # adding to crating detail tbl
                    for j in valid_package_id:
                        CratingDetail.objects.create(process_packaging_detail_id=j,
                                                     process_crating_master_id=crating_master.id,
                                                     scanned_by=user_id, status='crated')

                    # packaging detail table status change
                    PackagingDetail.objects.filter(id__in=valid_package_id).update(status='crated',
                                                                                   process_crating_master_id=crating_master.id)

                    return Response({'message': 'package crated successfully!', 'success': True,
                                     'crating_code': crating_code}, status=status.HTTP_201_CREATED)

            # if ONE of the bar_code invalid -> dont proceed
            else:
                print(f"invalid_bar_code > {invalid_bar_code}")
                return Response({'message': 'bar_code invalid!',
                                 'success': False,
                                 'invalid bar_code list': invalid_bar_code}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            error = 'online {}'.format(sys.exc_info()[-1].tb_lineno), e
            print(error)
            return Response({'message': "failed!", 'success': False}, status=status.HTTP_400_BAD_REQUEST)


class CratingDetailAPIView(APIView):

    def get(self, request):
        if 'user_id' not in request.data.keys() or request.data['user_id'] is '':
            raise ValidationError({'message': 'user_id is required', 'status_code': status.HTTP_400_BAD_REQUEST})
        if 'crating_code' not in request.data.keys() or request.data['crating_code'] is '':
            raise ValidationError({'message': 'crating_code is required', 'status_code': status.HTTP_400_BAD_REQUEST})

        try:
            crating_code = request.data['crating_code']

            try:
                crate = Crating.objects.get(crating_code=crating_code)
            except (ObjectDoesNotExist, PackagingDetail.MultipleObjectsReturned):
                return Response({'message': "invalid crating_code!", 'success': False},
                                status=status.HTTP_400_BAD_REQUEST)

            package = PackagingDetail.objects.filter(process_crating_master=crate)
            crating_serializer = CratingDetailSerializer(crate)
            packaging_detail_serializer = PackagingDetailSerializer(package, many=True)

            response = {"message": "success!",
                        'success': True,
                        'crating_detail': crating_serializer.data,
                        'packaging_detail': packaging_detail_serializer.data}

            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({'message': "failed!", 'success': False}, status=status.HTTP_400_BAD_REQUEST)


class ReadyShipmentAPIView(CreateAPIView):  # filter by status = ready ; created_by = request.data['user_id']
    serializer_class = ShippingInfoSerializer

    def post(self, request, **kwargs):
        if 'user_id' not in request.data.keys() or request.data['user_id'] is '':
            raise ValidationError({'success': False, 'message': 'user_id is required', 'status_code': status.HTTP_400_BAD_REQUEST})

        shipping = Shipping.objects.filter(status='ready', created_by=request.data['user_id'], delete_status=0).order_by('-pk')
        serializer = self.serializer_class(shipping, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ShipmentAddAPIView(CreateAPIView):
    serializer_class = ShippingInfoSerializer

    def post(self, request, **kwargs):
        if 'user_id' not in request.data.keys() or request.data['user_id'] is '':
            raise ValidationError({'success': False, 'message': 'user_id is required', 'status_code': status.HTTP_400_BAD_REQUEST})

        # user_id = request.data['user_id']
        shipping_code = generate_shipping_code()  # generate crate_no, bar_code
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(shipping_code=shipping_code)

        response = {
            'success': True,
            'status_code': status.HTTP_201_CREATED,
            'message': 'shipping info added successfully!',
            'shipping_code': shipping_code,
        }

        return Response(response, status=status.HTTP_201_CREATED)


class ShipmentEditAPIView(APIView):

    def put(self, request):
        if 'user_id' not in request.data.keys() or request.data['user_id'] is '':
            raise ValidationError({'message': 'user_id is required', 'status_code': status.HTTP_400_BAD_REQUEST})
        if 'shipping_id' not in request.data.keys() or request.data['shipping_id'] is '':
            raise ValidationError({'message': 'shipping_id is required', 'status_code': status.HTTP_400_BAD_REQUEST})

        try:
            user_id = request.data['user_id']
            shipping = Shipping.objects.get(id=request.data['shipping_id'], delete_status=0, status='ready')
            serializer = ShippingInfoSerializer(shipping, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(last_updated_by=user_id)
            return Response({'message': 'shipping info updated!', 'success': True}, status=status.HTTP_202_ACCEPTED)

        except ObjectDoesNotExist:
            return Response({'message': 'shipping_id not found', 'success': False}, status=status.HTTP_400_BAD_REQUEST)


class ShipmentDeleteAPIView(APIView):

    def put(self, request):
        if 'user_id' not in request.data.keys() or request.data['user_id'] is '':
            raise ValidationError({'message': 'user_id is required', 'status_code': status.HTTP_400_BAD_REQUEST})
        if 'shipping_id' not in request.data.keys() or request.data['shipping_id'] is '':
            raise ValidationError({'message': 'shipping_id is required', 'status_code': status.HTTP_400_BAD_REQUEST})

        try:
            user_id = request.data['user_id']
            shipping = Shipping.objects.get(id=request.data['shipping_id'], delete_status=0, status='ready')
            shipping.delete_status = 1
            shipping.last_updated_by = user_id
            shipping.save()
            return Response({'message': 'shipping info updated!', 'success': True}, status=status.HTTP_202_ACCEPTED)

        except ObjectDoesNotExist:
            return Response({'message': 'shipping_id not found', 'success': False}, status=status.HTTP_400_BAD_REQUEST)



class PackagingEditAPIView(APIView):
    @swagger_auto_schema(request_body=PackagingEditSerializer)
    # @access_permission_required
    def post(self, request):

        print(f"Received Data: {request.data}")

        try:
            with transaction.atomic():

                #  Update packaging table date
                transaction1 = Packaging.objects.filter(pk=request.data['packaging_id']).update(
                        packaging_unit=request.data['packaging_unit'],
                        packaging_unit_per_package=request.data['packaging_unit_per_package'],
                        total_no_of_sticker=request.data['total_no_of_sticker'],
                        last_updated_at=datetime.now(),
                        last_updated_by=request.data['user_id']
                    )

                # Deactivate existing stickers
                package_data = Packaging.objects.get(pk=request.data['packaging_id'])
                processing_id = package_data.processing_id
                packaging_detail = PackagingDetail.objects.filter(processing_id=processing_id)
                qr_code = packaging_detail[0].sticker_qr_code
                transaction2 = packaging_detail.update(status="deactivated")

                # Generate New sticker
                insert_data_to_packaging_detail(package_data, qr_code)
                return Response({"success": True,
                                 "message": 'Sticker generated successfully',
                                 "status_code": status.HTTP_201_CREATED},
                                status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({"success": False,
                             "message": f'Error! {e}',
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
