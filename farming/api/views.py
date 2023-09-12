from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import *
from farm.api.serializer import LandIdSerializer
from farming.models import Seeding, Land, Plot
from django.db.models import Sum
from rest_framework.validators import ValidationError
from drf_yasg.utils import swagger_auto_schema
from users.decorators import access_permission_required
from django.db import transaction
from datetime import datetime


# #####################Done before 21/01/2021########################
# class SeedingAddAPIView(APIView):
#
#     @swagger_auto_schema(request_body=SeedingSerializer)
#     @access_permission_required
#     def post(self, request):
#         print(f"Posted Data : {request.data}")
#         # request.data['status'] = 'ready'
#         # request.data['land'] = request.data['land_id']  # adding key 'land' to be consistent with model field name
#         # request.data['farmer'] = request.data['farmer_id']  # adding key 'farmer' to be consistent with model field name
#         seeding_data = {
#             'land': request.data['land_id'],
#             'farmer': request.data['farmer_id'],
#             'status': 'ready',
#             'seed_name': request.data['seed_name'],
#             # 'land_usage': request.data['land_usage'],
#             'created_by': request.data['created_by'],
#             'last_updated_by': request.data['last_updated_by'],
#             'sensor_data_seeding': request.data['sensor_data_seeding'],
#
#         }
#         serializer = SeedingSerializer(data=request.data)
#         if serializer.is_valid():
#             # check if the land is available for seeding & update land status
#             # current_land_usage = Seeding.objects.filter(land=request.data['land']).exclude\
#             #     (status__in=('fully harvested', 'damaged')).aggregate(Sum('land_usage'))
#
#             # print(f"current land usage: {current_land_usage}")
#             # if current_land_usage['land_usage__sum'] is None:
#             #     current_land_usage['land_usage__sum'] = 0
#             # land_usage = current_land_usage['land_usage__sum'] + request.data['land_usage']
#             # if land_usage < 100:
#                 # try:
#                 # Land.objects.filter(id=request.data['land']).update(
#                 #     status='partially occupied'
#                 # )
#                 # serializer.save()
#                 # return Response(status=status.HTTP_201_CREATED)
#                 # except ValueError:
#                 #     raise ValidationError({"message": "Land does not exists"})
#                 #     return Response(status=status.HTTP_400_BAD_REQUEST)
#
#             # elif land_usage == 100:
#             #     Land.objects.filter(id=request.data['land']).update(
#             #         status='fully occupied'
#             #     )
#             #     serializer.save()
#             #     return Response(status=status.HTTP_201_CREATED)
#             # else:
#             #     raise ValidationError({'message': 'land usage can not be higher than 100%'})
#             #     return Response(status=status.HTTP_400_BAD_REQUEST)
#             #     # return Response(status=status.HTTP_400_BAD_REQUEST)
#
#             update_land_table_status_with_seeding_create(request.data['land_id'], request.data['land_usage'])
#             # serializer.save()
#             res = Seeding.objects.create(
#                 land_id=seeding_data['land'],
#                 farmer_id=seeding_data['farmer'],
#                 status=seeding_data['status'],
#                 seed_name=seeding_data['seed_name'],
#                 land_usage=seeding_data['land_usage'],
#                 created_by=seeding_data['created_by'],
#                 last_updated_by=seeding_data['last_updated_by'],
#             )
#             print(f"Seeding id is {res.id}")
#             insert_to_plot_table(request.data, res.id)
#
#             return Response(status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SeedingAddAPIView(APIView):

    @swagger_auto_schema(request_body=SeedingSerializer)
    @access_permission_required
    def post(self, request):
        # print(f"Posted Data : {request.data}")
        land_id = request.data['land_id']
        land_available = check_if_land_is_free_for_seeding(land_id)
        if land_available is True:
            serializer = SeedingSerializer(data=request.data)
            if serializer.is_valid():
                # Check if optional values exists else assign a default value
                if 'seed_name' in request.data.keys():
                    seed_name = request.data['seed_name']
                else:
                    seed_name = ""
                if 'sensor_data_N' in request.data.keys():
                    sensor_data_N = request.data['sensor_data_N']
                else:
                    sensor_data_N = ""
                if 'sensor_data_P' in request.data.keys():
                    sensor_data_P = request.data['sensor_data_P']
                else:
                    sensor_data_P = ""
                if 'sensor_data_K' in request.data.keys():
                    sensor_data_K = request.data['sensor_data_K']
                else:
                    sensor_data_K = ""
                if 'max_no_of_plots' in request.data.keys():
                    max_no_of_plots = request.data['max_no_of_plots']
                else:
                    max_no_of_plots = 0
                # end of assigning default value to missing optional keys

                try:
                    with transaction.atomic():
                        # update land status to occupied
                        Land.objects.filter(id=request.data['land_id']).update(status="occupied")
                        Seeding.objects.create(
                            land_id=request.data['land_id'],
                            farmer_id=request.data['farmer_id'],
                            status="occupied",
                            seed_name=seed_name,
                            sensor_data_N=sensor_data_N,
                            sensor_data_P=sensor_data_P,
                            sensor_data_K=sensor_data_K,
                            created_by=request.data['user_id'],
                            last_updated_by=request.data['user_id'],
                            max_no_of_plots=max_no_of_plots
                        )
                        # print(f"Seeding id is {res.id}")
                        return Response({"success": True,
                                         "message": "Successfully Created",
                                         "status_code": status.HTTP_201_CREATED},
                                        status=status.HTTP_201_CREATED)

                except Exception as e:
                    print(e)
                    return Response({"success": False,
                                     "message": "Something went wrong!",
                                     "status_code": status.HTTP_400_BAD_REQUEST
                                     }, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({"success": False,
                                 "message": serializer.errors,
                                 "status_code": status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"success": False,
                             "message": "Land Already Occupied",
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)


def check_if_land_is_free_for_seeding(land_id):
    print(f"Land is {land_id} & type {type(land_id)}")
    try:
        land = Land.objects.get(id=land_id, is_active=1)
    except Exception as e:
        print(e)
        return False
    land_status = land.status
    if land_status == "ready":
        return True
    else:
        return False


# class PlotAddAPIView(APIView):
#     @swagger_auto_schema(request_body=PlotSerializer)
#     @access_permission_required
#     def post(self, request):
#         request.data['crop_status'] = 'ready'
#         serializer = PlotSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class PlotStatusAPIView(APIView):
#     @swagger_auto_schema(request_body=PlotStatusSerializer)
#     def put(self, request):
#         if 'plot_id' in request.data.keys() and 'plot_status' in request.data.keys():
#             plot_id = request.data['plot_id']
#             new_status = request.data['plot_status']
#             update_by = request.data['update_by']
#             update_at = request.data['update_at']
#             print(f"Status updated on {update_at}")
#             # get plot object
#             try:
#                 plot = Plot.objects.get(id=plot_id)
#             except Plot.DoesNotExist:
#                 raise ValidationError({"message": "Invalid plot!"})
#                 return Response(status=status.HTTP_400_BAD_REQUEST)
#             if new_status == "damaged":
#                 update_land_usage_in_seeding_table(plot.seeding_id)
#                 plot.crop_status = "damaged"
#                 plot.last_updated_by = update_by
#                 plot.last_updated_at = update_at
#                 plot.save()
#                 insert_to_log_table(plot_id, new_status, update_by, update_at)
#                 update_seeding_table_status(plot.seeding_id)
#
#                 return Response(status=status.HTTP_202_ACCEPTED)
#             elif new_status == "ready":
#                 plot.crop_status = "ready"
#                 plot.last_updated_by = update_by
#                 plot.last_updated_at = update_at
#                 plot.save()
#                 insert_to_log_table(plot_id, new_status, update_by, update_at)
#                 update_seeding_table_status(plot.seeding_id)
#                 return Response(status=status.HTTP_202_ACCEPTED)
#             elif new_status == "growing":
#                 # Plot.objects.filter(id=plot_id).update(crop_status="growing")
#                 plot.crop_status = "growing"
#                 plot.last_updated_by = update_by
#                 plot.last_updated_at = update_at
#                 plot.save()
#                 insert_to_log_table(plot_id, new_status, update_by, update_at)
#                 update_seeding_table_status(plot.seeding_id)
#                 return Response(status=status.HTTP_202_ACCEPTED)
#             elif new_status == "partially harvested":
#                 plot.crop_status = "partially harvested"
#                 plot.last_updated_by = update_by
#                 plot.last_updated_at = update_at
#                 plot.save()
#                 insert_to_log_table(plot_id, new_status, update_by, update_at)
#                 update_seeding_table_status(plot.seeding_id)
#                 return Response(status=status.HTTP_202_ACCEPTED)
#             elif new_status == "fully harvested":
#                 update_land_usage_in_seeding_table(plot.seeding_id)
#                 plot.crop_status = "fully harvested"
#                 plot.last_updated_by = update_by
#                 plot.last_updated_at = update_at
#                 plot.save()
#                 insert_to_log_table(plot_id, new_status, update_by, update_at)
#                 update_seeding_table_status(plot.seeding_id)
#                 return Response(status=status.HTTP_202_ACCEPTED)
#             else:
#                 raise ValidationError({"message": "Invalid plot status!"})
#                 return Response(status=status.HTTP_400_BAD_REQUEST)
#         else:
#             # raise ValidationError({"message": "Invalid key"})
#             return Response(status=status.HTTP_400_BAD_REQUEST)


# def insert_to_log_table(plot_id, new_status, update_by, update_at):
#     try:
#         PlotStatusLog.objects.create(
#             plot_id=plot_id,
#             crop_status=new_status,
#             # created_by=None,
#             # created_at=None,
#             last_updated_by=update_by,
#             last_updated_at=update_at
#         )
#     except Exception as e:
#         print(e)


# def update_seeding_table_status(seeding_id):
#     # find lowest status of plot under the seeding_id
#     land_id = Seeding.objects.get(id=seeding_id).land_id
#     plot_status_dict = Plot.objects.filter(seeding=seeding_id).values('crop_status').distinct()
#     print(f"plot status_dict {plot_status_dict}")
#     plot_status_list = []
#     for data in plot_status_dict:
#         plot_status_list.append(data['crop_status'])  # list of all distinct plot status
#
#     if all(x == "damaged" for x in plot_status_list):
#         print("seeding status: damaged")
#         Seeding.objects.filter(id=seeding_id).update(status="damaged")
#         # print("update overall land status")
#         update_land_table_status_with_seeding_status(land_id)
#     elif any(x == "ready" for x in plot_status_list):
#         print("seeding status : ready")
#         Seeding.objects.filter(id=seeding_id).update(status="ready")
#         update_land_table_status_with_seeding_status(land_id)
#     elif any(x == "growing" for x in plot_status_list):
#         print("seeding status: growing")
#         Seeding.objects.filter(id=seeding_id).update(status="growing")
#         update_land_table_status_with_seeding_status(land_id)
#     elif any(x == "partially harvested" for x in plot_status_list):
#         print("seeding status: partially harvested")
#         Seeding.objects.filter(id=seeding_id).update(status="partially harvested")
#         update_land_table_status_with_seeding_status(land_id)
#     elif any(x == "fully harvested" for x in plot_status_list):
#         print("seeding status : fully harvested")
#         Seeding.objects.filter(id=seeding_id).update(status="fully harvested")
#         update_land_table_status_with_seeding_status(land_id)


# print(f"Seeding serializer: {PlotSerializer(plot_status_dict).data}")
# for data in plot_status_dict:
#     if all(x == "damaged" for x in data.values()):
#         print("update seeding status to damaged")
#     elif any(x == "growing" for x in data.values()):
#         print("update seeding status to growing")
#     elif any(x == "partially harvested" for x in data.values()):
#         print("update seeding status to partially harvested")
#     elif any(x == "fully harvested" for x in data.values()):
#         print("update seeding status to fully harvested")
#     else:
#         print("update seeding status to ready")
# for data in plot_status_dict:
#     if data['crop_status'] == "ready":
#         status = "ready"
# for data in plot_status_dict:
#     if data['crop_status'] == 'ready':
#         seeding_status = 'ready'
#         break
#     elif data['crop_status'] == 'growing':
#         seeding_status = 'growing'
#         break
#     elif data['crop_status'] == 'partially harvested':
#         seeding_status = 'partially harvested'
#         break
#     elif data['crop_status'] == 'fully harvested':
#         seeding_status = 'fully harvested'
#         break

# print(plot_status_list)


def update_land_table_status_with_seeding_status(land_id):
    """
    Update land table status column based on
    seeding table status change

    """

    current_land_usage = Seeding.objects.filter(land_id=land_id).exclude(status__in=('fully harvested', 'damaged')). \
        aggregate(Sum('land_usage'))
    seeding_status_dict = Seeding.objects.filter(land_id=land_id).values('status').distinct()
    print(f"seeding_status_dict {seeding_status_dict}")
    seeding_status_list = []
    for data in seeding_status_dict:
        seeding_status_list.append(data['status'])  # list of all distinct seeding status

    if all(x == "damaged" for x in seeding_status_list):
        print("all seeding status: damaged")
        Land.objects.filter(id=land_id).update(status="free")

    elif all(x == "fully harvested" for x in seeding_status_list):
        print("all seeding status: fully harvested")
        Land.objects.filter(id=land_id).update(status="free")

    elif "ready" in seeding_status_list or "growing" in seeding_status_list or "partially harvested" \
            in seeding_status_list:
        if current_land_usage['land_usage__sum'] == 100:
            Land.objects.filter(id=land_id).update(status="fully occupied")
        else:
            Land.objects.filter(id=land_id).update(status="partially occupied")
    # elif any(x == "ready" for x in seeding_status_list):
    #     print("At least one seeding status : ready")
    #     Land.objects.filter(id=land_id).update(status="partially occupied")
    # elif any(x == "growing" for x in seeding_status_list):
    #     print("At least one seeding status: growing")
    #     Land.objects.filter(id=land_id).update(status="partially occupied")
    # elif any(x == "partially harvested" for x in seeding_status_list):
    #     print("At least one seeding status: partially harvested")
    #     Land.objects.filter(id=land_id).update(status="partially occupied")


# def single_plot_percentage(seeding_id):
#     no_of_active_plot = Plot.objects.filter(seeding_id=seeding_id).count()
#     total_percentage_occupied = Seeding.objects.get(id=seeding_id).land_usage
#     plot_percentage = round(total_percentage_occupied/no_of_active_plot, 2)
#     return plot_percentage


def update_land_usage_in_seeding_table(seeding_id):
    current_percentage_occupied = Seeding.objects.get(id=seeding_id).land_usage  # by a single seeding
    no_of_active_plot = Plot.objects.filter(seeding_id=seeding_id). \
        exclude(crop_status__in=('damaged', 'fully harvested')).count()  # of a particular seeding
    single_plot_percentage = round(current_percentage_occupied / no_of_active_plot, 2)
    updated_percentage_occupied = current_percentage_occupied - single_plot_percentage

    # update in db
    Seeding.objects.filter(id=seeding_id).update(land_usage=updated_percentage_occupied)


# class PlotEditAPIView(APIView):
#     @swagger_auto_schema(request_body=PlotSerializer)
#     @access_permission_required
#     def put(self, request):
#         print(f"Plain data: {request.data}")
#         if 'plot_id' not in request.data.keys() or request.data['plot_id'] is '' \
#                 or 'plot_status' in request.data.keys():
#             # raise ValidationError({'message': 'plot_id is required', 'status_code': '400'})
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         else:
#             try:
#                 plot = Plot.objects.get(id=request.data['plot_id'])
#             except Plot.DoesNotExist:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#
#             serializer = PlotSerializer(plot, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 # return Response(serializer.data)
#                 return Response(status=status.HTTP_202_ACCEPTED)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SeedingEditAPIView(APIView):
#     @swagger_auto_schema(request_body=SeedingSerializer)
#     @access_permission_required
#     def put(self, request):
#         print(f"Plain data: {request.data}")
#         if 'seeding_id' not in request.data.keys() or request.data['seeding_id'] is '':
#
#             # raise ValidationError({'message': 'seeding_id is required', 'status_code': '400'})
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         else:
#             try:
#                 seeding = Seeding.objects.get(id=request.data['seeding_id'])
#             except Seeding.DoesNotExist:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#             # request.data['land_usage'] = seeding.land_usage
#             request.data['land'] = request.data['land_id']  # adding key 'land' to be consistent with model field name
#             serializer = SeedingSerializer(seeding, data=request.data)
#             if serializer.is_valid():
#                 update_land_table_status_with_seeding_create(request.data['land'], request.data['land_usage'])
#                 serializer.save()
#                 return Response(status=status.HTTP_202_ACCEPTED)
#                 # current_land_usage = Seeding.objects.filter(land=request.data['land_id']).exclude \
#                 #     (status__in=('fully harvested', 'damaged')).aggregate(Sum('land_usage'))
#                 # print(f"current land usage: {current_land_usage}")
#                 # if current_land_usage['land_usage__sum'] is None:
#                 #     current_land_usage['land_usage__sum'] = 0
#                 # land_usage = current_land_usage['land_usage__sum'] + request.data['land_usage']
#                 # if land_usage < 100:
#                 #     # try:
#                 #     Land.objects.filter(id=request.data['land']).update(
#                 #         status='partially occupied'
#                 #     )
#                 #     serializer.save()
#                 #     return Response(status=status.HTTP_202_ACCEPTED)
#                 #     # except ValueError:
#                 #     #     raise ValidationError({"message": "Land does not exists"})
#                 #     #     return Response(status=status.HTTP_400_BAD_REQUEST)
#                 #
#                 # elif land_usage == 100:
#                 #     Land.objects.filter(id=request.data['land']).update(
#                 #         status='fully occupied'
#                 #     )
#                 #     serializer.save()
#                 #     return Response(status=status.HTTP_201_CREATED)
#                 # else:
#                 #     raise ValidationError({'message': 'land usage can not be higher than 100%'})
#                 #     return Response(status=status.HTTP_400_BAD_REQUEST)
#                     # return Response(status=status.HTTP_400_BAD_REQUEST)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def update_land_table_status_with_seeding_create(land_id, land_usage):
#     current_land_usage = Seeding.objects.filter(land_id=land_id).exclude \
#         (status__in=('fully harvested', 'damaged')).aggregate(Sum('land_usage'))
#
#     if current_land_usage['land_usage__sum'] is None:
#         current_land_usage['land_usage__sum'] = 0
#
#     requested_land_usage = current_land_usage['land_usage__sum'] + land_usage
#     print(f"Requested land usage: {requested_land_usage}")
#     if requested_land_usage < 100:
#         # try:
#         Land.objects.filter(id=land_id).update(
#             status='partially occupied'
#         )
#     elif requested_land_usage == 100:
#         Land.objects.filter(id=land_id).update(
#             status='fully occupied'
#         )
#     else:
#         raise ValidationError({'message': 'land usage can not be higher than 100%'})
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# class SeedingStatusAPIView(APIView):
#     @swagger_auto_schema(request_body=LandStatusSerializer)
#     @access_permission_required
#     def put(self, request):
#         if 'land_id' in request.data.keys() and 'land_status' in request.data.keys():
#             land_id = request.data['land_id']
#             land_status = request.data['land_status']
#             update_by = request.data['update_by']
#             update_at = request.data['update_at']
#             print(f"Status updated on {update_at}")
#             # get plot object
#             try:
#                 land = Land.objects.get(id=land_id)
#             except Land.DoesNotExist:
#                 # raise ValidationError({"message": "Invalid Land!"})
#                 return Response(status=status.HTTP_400_BAD_REQUEST)
#             if land_status == "damaged":
#                 land.status = "free"
#                 land.last_updated_by = update_by
#                 land.last_updated_at = update_at
#                 land.save()
#                 # get seeding under the land the specified land_id
#                 seeding_queryset = Seeding.objects.filter(land_id=land_id). \
#                     exclude(status__in=('fully harvested', 'damaged'))
#                 # force the execution of the queryset by list()
#                 # plots_list = list(Plot.objects.filter(seeding__in=seeding_queryset))
#                 plots_queryset = Plot.objects.filter(seeding__in=seeding_queryset)
#                 plots_queryset.update(crop_status='damaged', last_updated_by=update_by, last_updated_at=update_at)
#                 # print(f"plots: {plots_list}")
#                 # for data in plots_queryset:
#                 # print(f"plot id: {data.id}")
#                 # PlotStatusLog.objects.create(
#                 #     plot_id=data.id,
#                 #     last_updated_by=update_by,
#                 #     last_updated_at=update_at,
#                 #     crop_status='damaged'
#                 # )
#                 seeding_queryset.update(status='damaged', last_updated_by=update_by, last_updated_at=update_at)
#
#                 return Response(status=status.HTTP_202_ACCEPTED)
#             else:
#                 # raise ValidationError({"message": "Invalid land status"})
#                 return Response(status=status.HTTP_400_BAD_REQUEST)


class SeedingListAPIView(APIView):
    @swagger_auto_schema(request_body=LandIdSerializer)
    @access_permission_required
    def post(self, request):
        if 'land_id' in request.data.keys():
            seeding = Seeding.objects.filter(land_id=request.data['land_id'])

            serializer = SeedingListSerializer(seeding, many=True)
            # print(f"Serializer : {serializer}")
            return Response({"success": True,
                             "seeding_list": serializer.data,
                             "status_code": status.HTTP_200_OK
                             }, status=status.HTTP_200_OK
                            )
        else:
            return Response({"success": False,
                             "message": "Please provide land_id",
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)


class PlotListAPIView(APIView):
    @swagger_auto_schema(request_body=SeedingIdSerializer)
    @access_permission_required
    def post(self, request):
        if 'seeding_id' in request.data.keys():
            # get all plots under the seeding
            try:
                plot = Plot.objects.filter(seeding=request.data['seeding_id'])
                serializer = PlotListSerializer(plot, many=True)
                # print(f"Serializer : {serializer}")
                return Response({"success": True,
                                 "plot_list": serializer.data,
                                 "status_code": status.HTTP_200_OK
                                 }, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response({"success": False,
                                 "message": f"Error! {e}",
                                 "status_code": status.HTTP_400_BAD_REQUEST
                                 }, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"success": False,
                             "message": f"seeding_id is required",
                             "status_code": status.HTTP_400_BAD_REQUEST
                             }, status=status.HTTP_400_BAD_REQUEST)


def insert_to_plot_table(data, seeding_id):
    print(f"Data: {data}")
    no_of_plots = int(data['no_of_plots'])
    # List of plot table columns which may or may not be filled by user
    plot_table_optional_columns = ['costing', 'expected_harvesting_time', 'fertilizers', 'sensor_data_seeding',
                                   'sensor_data_harvesting', 'comment']
    for col in plot_table_optional_columns:
        if col in data.keys():
            pass    # if the col is filled keep the value
        else:
            data[col] = 0  # else assign 0 the column

    for i in range(0, no_of_plots):
        try:
            Plot.objects.create(
                seeding_id=seeding_id,
                costing=data['costing'],
                expected_harvesting_time=data['expected_harvesting_time'],
                status='ready',
                crop_id=data['crop_id'],
                crop_type_id=data['crop_type_id'],
                crop_variant=data['crop_variant_id'],
                fertilizers=data['fertilizers'],
                created_by=data['created_by'],
                last_updated_by=data['last_updated_by'],
                sensor_data_seeding=data['sensor_data_seeding'],
                sensor_data_harvesting=data['sensor_data_harvesting'],
                comment=data['comment']
            )
        except Exception as e:
            print(e)


# class HarvestingAddAPIView(APIView):
#     @swagger_auto_schema(request_body=HarvestingSerializer)
#     @access_permission_required
#     def post(self, request):
#         print(f"Posted Data : {request.data}")
#         # check if plot is valid for harvesting
#         try:
#             seeding_status = Seeding.objects.get(id=request.data['seeding']).status
#             if seeding_status == "fully harvested":
#                 raise ValidationError({'message': 'seeding fully harvested'})
#                 return Response(status=status.HTTP_400_BAD_REQUEST)
#         except Seeding.DoesNotExist:
#             raise ValidationError({'message': 'invalid seeding id'})
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         serializer = HarvestingSerializer(data=request.data)
#         if serializer.is_valid():
#             # find harvest_cycle
#
#             harvest_cycle = Harvesting.objects.filter(seeding=request.data['seeding']).count()
#             if harvest_cycle == 0:
#                 harvest_cycle = 1
#             else:
#                 harvest_cycle += 1
#
#             print(f"harvest_cycle: {harvest_cycle}")
#             serializer.save(harvest_cycle=harvest_cycle)
#             harvest_status = request.data['status']
#             print(f"Harvesting status: {harvest_status}")
#             if harvest_status == "partially harvested":
#                 Seeding.objects.filter(id=request.data['seeding']).update(status="partially harvested")
#                 Plot.objects.filter(seeding_id=request.data['seeding']).update(status="partially harvested")
#                 return Response(status=status.HTTP_202_ACCEPTED)
#             elif harvest_status == "fully harvested":
#                 Seeding.objects.filter(id=request.data['seeding']).update(status="fully harvested")
#                 Plot.objects.filter(seeding_id=request.data['seeding']).update(status="fully harvested")
#                 # update_land_usage_in_seeding_table(request.data['seeding_id'])
#                 land_id = Seeding.objects.get(id=request.data['seeding']).land_id
#                 update_land_table_status_with_seeding_status(land_id)
#                 return Response(status=status.HTTP_202_ACCEPTED)
#
#             return Response(status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class HarvestingEditAPIView(APIView):
#     @swagger_auto_schema(request_body=HarvestingSerializer)
#     @access_permission_required
#     def put(self, request):
#         print(f"Plain data: {request.data}")
#         if 'harvesting_id' not in request.data.keys() or request.data['harvesting_id'] is '':
#
#             # raise ValidationError({'message': 'seeding_id is required', 'status_code': '400'})
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         else:
#             try:
#                 harvesting = Harvesting.objects.get(id=request.data['harvesting_id'])
#             except Harvesting.DoesNotExist:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#             # request.data['land_usage'] = seeding.land_usage
#             serializer = HarvestingSerializer(harvesting, data=request.data)
#         if serializer.is_valid():
#             # print(f"Posted Data : {request.data}")
#             # serializer = HarvestingSerializer(data=request.data)
#             # if serializer.is_valid():
#             serializer.save()
#             harvest_status = request.data['status']
#             print(f"Harvesting status: {harvest_status}")
#             if harvest_status == "partially harvested":
#                 Seeding.objects.filter(id=request.data['seeding_id']).update(status="partially harvested")
#                 Plot.objects.filter(seeding_id=request.data['seeding_id']).update(status="partially harvested")
#                 return Response(status=status.HTTP_202_ACCEPTED)
#             elif harvest_status == "fully harvested":
#                 Seeding.objects.filter(id=request.data['seeding_id']).update(status="fully harvested")
#                 Plot.objects.filter(seeding_id=request.data['seeding_id']).update(status="fully harvested")
#                 # update_land_usage_in_seeding_table(request.data['seeding_id'])
#                 land_id = Seeding.objects.get(id=request.data['seeding_id']).land_id
#                 update_land_table_status_with_seeding_status(land_id)
#                 return Response(status=status.HTTP_202_ACCEPTED)
#
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SeedingEditAPIView(APIView):
    @swagger_auto_schema(request_body=SeedingEditSerializer)
    @access_permission_required
    def put(self, request):
        seeding_id = request.data['seeding_id']
        # check if seeding id is valid
        try:
            Seeding.objects.get(id=seeding_id, status__in=['ready', 'occupied'])
        except Seeding.DoesNotExist:
            return Response({"success": False,
                             "message": "Invalid seeding_id",
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
        # check if new max_no_of_plots is valid i.e greater or equal to existing active plots
        active_plot_count = Plot.objects.filter(seeding_id=seeding_id,
                                                status__in=['ready', 'partially harvested']).count()
        print(f"active plot count: {active_plot_count} & type: {type(active_plot_count)}")
        print(f"max_no_of_plots: { request.data['max_no_of_plots']} & type: {type(request.data['max_no_of_plots'])}")

        if active_plot_count > request.data['max_no_of_plots']:
            return Response({"success": False,
                             "message": "No. of plots can't be less then currently active plots",
                             "status_code": status.HTTP_400_BAD_REQUEST
                             }, status=status.HTTP_400_BAD_REQUEST)
        serializer = SeedingSerializer(data=request.data)
        if serializer.is_valid():
            # Check if optional values exists else assign a default value
            if 'seed_name' in request.data.keys():
                seed_name = request.data['seed_name']
            else:
                seed_name = ""
            if 'sensor_data_N' in request.data.keys():
                sensor_data_N = request.data['sensor_data_N']
            else:
                sensor_data_N = ""
            if 'sensor_data_P' in request.data.keys():
                sensor_data_P = request.data['sensor_data_P']
            else:
                sensor_data_P = ""
            if 'sensor_data_K' in request.data.keys():
                sensor_data_K = request.data['sensor_data_K']
            else:
                sensor_data_K = ""
            if 'max_no_of_plots' in request.data.keys():
                max_no_of_plots = request.data['max_no_of_plots']
            else:
                max_no_of_plots = 0
            # end of assigning default value to missing optional keys

            try:
                Seeding.objects.filter(id=seeding_id).update(
                    land_id=request.data['land_id'],
                    farmer_id=request.data['farmer_id'],
                    status="occupied",
                    seed_name=seed_name,
                    sensor_data_N=sensor_data_N,
                    sensor_data_P=sensor_data_P,
                    sensor_data_K=sensor_data_K,
                    last_updated_by=request.data['user_id'],
                    max_no_of_plots=max_no_of_plots
                )
                # print(f"Seeding id is {res.id}")
                return Response({"success": True,
                                 "message": "Successfully Updated",
                                 "status_code": status.HTTP_201_CREATED},
                                status=status.HTTP_201_CREATED)

            except Exception as e:
                print(e)
                return Response({"success": False,
                                 "message": "Something went wrong!",
                                 "status_code": status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"success": False,
                             "message": f"Error: {serializer.errors}",
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)


class PlotAddAPIView(APIView):
    @swagger_auto_schema(request_body=PlotSerializer)
    @access_permission_required
    def post(self, request):
        seeding_id = request.data['seeding']
        # check valid seeding id
        try:
            max_no_of_plots = Seeding.objects.get(pk=seeding_id).max_no_of_plots
        except Seeding.DoesNotExist:
            return Response({"success": False,
                             "message": "Invalid seeding id",
                             "status_code": status.HTTP_400_BAD_REQUEST
                             },
                            status=status.HTTP_400_BAD_REQUEST)
        # check if new plot creation is allowed (from max_no_of_plots of corresponding seeding i.e count active plots
        # under a seeding)
        active_plot_count = Plot.objects.filter(seeding_id=seeding_id,
                                                status__in=['ready', 'partially harvested']).count()
        if max_no_of_plots == active_plot_count:
            return Response({"success": False,
                             "message": "All plots under the seeding is already created!",
                             "status_code": status.HTTP_400_BAD_REQUEST
                             },
                            status=status.HTTP_400_BAD_REQUEST)
        # check % of land usage of all active plot under a seeding. Maximum allowed % is 100%
        current_land_usage = Plot.objects.filter(seeding_id=seeding_id, status__in=['ready', 'partially harvested']). \
            aggregate(Sum('land_usage'))
        if current_land_usage['land_usage__sum'] is None:  # when no plot is created yet
            current_land_usage['land_usage__sum'] = 0
        total_land_usage = current_land_usage['land_usage__sum'] + request.data['land_usage']
        if total_land_usage > 100:
            return Response({"success": False,
                             "message": "Summation of Land Usage of all plots under a "
                                        "seeding can't be higher then 100%",
                             "status_code": status.HTTP_400_BAD_REQUEST
                             },
                            status=status.HTTP_400_BAD_REQUEST)

        # if all the above is passed then allow new plot creation

        serializer = PlotSerializer(data=request.data)
        # print(serializer)
        if serializer.is_valid():
            # serializer.save(create_by=request.data['user_id'], last_updated_by=request.data['last_updated_by'])

            # serializer.save(status="ready")
            # serializer.save(created_by=request.data['user_id'], last_updated_by=request.data['user_id'])
            try:
                Plot.objects.create(
                    seeding_id=request.data['seeding'],
                    seed_procurement=request.data['seed_procurement'],
                    costing=request.data['costing'],
                    expected_harvesting_time=request.data['expected_harvesting_time'],
                    start_time=request.data['start_time'],
                    # default crop_status: ready, partially harvested, fully harvested, damaged
                    status="ready",
                    total_labor_hour=request.data['total_labor_hour'],
                    crop_id=request.data['crop'],
                    crop_type_id=request.data['crop_type'],
                    crop_variant=request.data['crop_variant'],
                    fertilizers=request.data['fertilizers'],
                    created_by=request.data['user_id'],
                    last_updated_by=request.data['user_id'],
                    land_usage=request.data['land_usage']

                )
                return Response({"success": True,
                                 "message": "Plot Created Successfully",
                                 "status_code": status.HTTP_201_CREATED
                                 },
                                status=status.HTTP_201_CREATED)
            except Exception as e:
                print(e)
                return Response({"success": False,
                                 "message": f"Error: {e}",
                                 "status_code": status.HTTP_400_BAD_REQUEST
                                 },
                                status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"success": False,
                             "message": f"Error: {serializer.errors}",
                             "status_code": status.HTTP_400_BAD_REQUEST
                             },
                            status=status.HTTP_400_BAD_REQUEST)


class PlotEditAPIView(APIView):
    @swagger_auto_schema(request_body=PlotEditSerializer)
    @access_permission_required
    def put(self, request):
        # check for valid plot id
        plot_id = request.data['plot_id']
        try:
            Plot.objects.get(pk=plot_id)
        except Plot.DoesNotExist:
            return Response({"success": False,
                             "message": 'Invalid plot_id',
                             "status": status.HTTP_400_BAD_REQUEST
                             },
                            status=status.HTTP_404_NOT_FOUND)

        # check valid seeding id
        seeding_id = request.data['seeding']
        try:
            Seeding.objects.get(pk=seeding_id)
        except Seeding.DoesNotExist:
            return Response({"success": False,
                             "message": "Invalid seeding id",
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
        # check % of land usage of all active plot under a seeding Excluding the plot to be edited.
        # Maximum allowed % is 100%
        current_land_usage = Plot.objects.filter(seeding_id=seeding_id, status__in=['ready', 'partially harvested']). \
            exclude(pk=plot_id).aggregate(Sum('land_usage'))
        print(f"current_land_usage: {current_land_usage}")
        print(f"current_land_usage['land_usage__sum']: {current_land_usage['land_usage__sum']}")
        # if current_land_usage['land_usage__sum'] is None:
        #     current_land_usage['land_usage__sum'] = 0
        total_land_usage = current_land_usage['land_usage__sum'] + request.data['land_usage']
        if total_land_usage > 100:
            return Response({"success": False,
                             "message": "Summation of Land Usage of all plots under a "
                                        "seeding can't be higher then 100%",
                             "status_code": status.HTTP_400_BAD_REQUEST
                             },
                            status=status.HTTP_400_BAD_REQUEST)

            # if all the above is passed then allow  plot edit

        serializer = PlotSerializer(data=request.data)
        # print(serializer)
        if serializer.is_valid():
            # serializer.save(create_by=request.data['user_id'], last_updated_by=request.data['last_updated_by'])

            # serializer.save(status="ready")
            # serializer.save(created_by=request.data['user_id'], last_updated_by=request.data['user_id'])
            try:
                Plot.objects.filter(pk=plot_id).update(
                    seeding_id=request.data['seeding'],
                    seed_procurement=request.data['seed_procurement'],
                    costing=request.data['costing'],
                    expected_harvesting_time=request.data['expected_harvesting_time'],
                    start_time=request.data['start_time'],
                    # default crop_status: ready, partially harvested, fully harvested, damaged
                    status="ready",
                    total_labor_hour=request.data['total_labor_hour'],
                    crop_id=request.data['crop'],
                    crop_type_id=request.data['crop_type'],
                    crop_variant=request.data['crop_variant'],
                    fertilizers=request.data['fertilizers'],
                    created_by=request.data['user_id'],
                    last_updated_by=request.data['user_id'],
                    land_usage=request.data['land_usage']

                )
                return Response({"success": True,
                                 "message": "Plot Updated Successfully",
                                 "status_code": status.HTTP_202_ACCEPTED
                                 },
                                status=status.HTTP_202_ACCEPTED)
            except Exception as e:
                print(e)
                return Response({"success": False,
                                 "message": f"Error: {e}",
                                 "status_code": status.HTTP_400_BAD_REQUEST
                                 },
                                status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"success": False,
                             "message": f"Error: {serializer.errors}",
                             "status_code": status.HTTP_400_BAD_REQUEST
                             },
                            status=status.HTTP_400_BAD_REQUEST)

            # serializer = PlotSerializer(plot, data=request.data)
            # if serializer.is_valid():
            #     serializer.save()
            #     # return Response(serializer.data)
            #     return Response(status=status.HTTP_202_ACCEPTED)
            # else:
            #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            #


class PlotStatusUpdateAPIView(APIView):

    @swagger_auto_schema(request_body=PlotStatusSerializer)
    @access_permission_required
    def put(self, request):
        if 'plot_id' in request.data.keys() and 'plot_status' in request.data.keys():
            plot_id = request.data['plot_id']
            new_status = request.data['plot_status']
            try:
                Plot.objects.get(id=plot_id)
            except Plot.DoesNotExist:
                return Response({"success": False,
                                 "message": 'Invalid plot_id',
                                 "status_code": status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)

            print(f"New status: {new_status} & type: {type(new_status)}")
            if new_status == "partially harvested" or new_status == "fully harvested":
                try:
                    Plot.objects.filter(pk=plot_id).update(
                        status=new_status,
                        last_updated_by=request.data['user_id'],
                        last_updated_at=datetime.now()
                    )
                    return Response({
                        "success": True,
                        "message": "Status updated successfully",
                        "status_code": status.HTTP_200_OK
                    }, status=status.HTTP_200_OK)
                except Exception as e:
                    return Response({
                        "success": False,
                        "message": f'Error: {e}',
                        "status_code": status.HTTP_400_BAD_REQUEST
                    }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"success": False,
                                 "message": 'Invalid status',
                                 "status_code": status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"success": False,
                             "message": 'plot_id and/or plot_status is required',
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)


class HarvestingAddAPIView(APIView):
    @swagger_auto_schema(request_body=HarvestingSerializer)
    @access_permission_required
    def post(self, request):
        print(f"Posted Data : {request.data}")
        # check if plot_id is valid
        try:
            plot_status = Plot.objects.get(id=request.data['plot_id']).status
        except Plot.DoesNotExist:
            return Response({
                "success": False,
                "message": 'Invalid plot id',
                "status_code": status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)

        # check if plot is valid for harvesting
        if plot_status == "fully harvested":
            return Response({
                "success": False,
                "message": 'plot already fully harvested',
                "status_code": status.HTTP_400_BAD_REQUEST},
                status=status.HTTP_400_BAD_REQUEST)

        # check if harvest quantity is integer
        try:
            int(request.data['quantity'])
        except ValueError:
            return Response({
                "success": False,
                "message": 'Invalid harvest quantity; it must be an integer',
                "status_code": status.HTTP_400_BAD_REQUEST},
                status=status.HTTP_400_BAD_REQUEST)

        # if above 3 condition is passed then create harvest
        serializer = HarvestingSerializer(data=request.data)
        if serializer.is_valid():
            # find harvest_cycle
            harvest_cycle = Harvesting.objects.filter(plot_id=request.data['plot_id']).count()
            if harvest_cycle == 0:
                harvest_cycle = 1
            else:
                harvest_cycle += 1

            print(f"harvest_cycle: {harvest_cycle}")
            # serializer.save(harvest_cycle=harvest_cycle)

            # create new harvesting rows and
            with transaction.atomic():
                try:
                    harvest_obj = Harvesting.objects.create(
                        plot_id=request.data['plot_id'],
                        harvest_cycle=harvest_cycle,
                        crop_status=request.data['crop_status'],
                        total_labor_hour=request.data['total_labor_hour'],
                        farmer_id=request.data['farmer'],
                        quantity=request.data['quantity'],
                        status=request.data['status'],
                        created_at=datetime.now(),
                        created_by=request.data['user_id'],
                        last_updated_by=request.data['user_id'],
                        sensor_data_N=request.data['sensor_data_N'],
                        sensor_data_P=request.data['sensor_data_P'],
                        sensor_data_K=request.data['sensor_data_K']
                    )

                    harvest_id = harvest_obj.id
                    # update this harvest id in plot table
                    Plot.objects.filter(pk=request.data['plot_id']).update(harvest_id=harvest_id)
                except Exception as e:
                    return Response({
                        "success": False,
                        "message": f'Error! {e}',
                        "status_code": status.HTTP_400_BAD_REQUEST

                    }, status=status.HTTP_400_BAD_REQUEST)

            # update plot status based on harvest status
            harvest_status = request.data['status']
            print(f"Harvesting status: {harvest_status}")
            if harvest_status == "partially harvested":
                # update only plot status to "partially harvested"
                Plot.objects.filter(pk=request.data['plot_id']).update(status="partially harvested")
                return Response({"success": True,
                                 "message": 'Harvest added successfully',
                                 "status_code": status.HTTP_202_ACCEPTED},
                                status=status.HTTP_202_ACCEPTED)

            # update plot , seeding and land status (if fully harvested)
            elif harvest_status == "fully harvested":
                Plot.objects.filter(pk=request.data['plot_id']).update(status="fully harvested")
                # if active plot count is 0 then close the seeding and make the land free
                seeding_id = Plot.objects.get(pk=request.data['plot_id']).seeding.id  # get seeding id
                active_plot_count = Plot.objects.filter(seeding_id=seeding_id,
                                                        status__in=['ready', 'partially harvested']).count()
                if active_plot_count == 0:
                    seeding_obj = Seeding.objects.filter(pk=seeding_id)
                    seeding_obj.update(status="closed")  # update seeding status
                    land_id = seeding_obj[0].land.id
                    Land.objects.filter(pk=land_id).update(status="ready")
                    return Response({"success": True,
                                     "message": 'Harvest added successfully',
                                     "status_code": status.HTTP_202_ACCEPTED})

                # if active plot count != 0 than just return
                else:
                    return Response({"success": True,
                                     "message": 'Harvest added successfully',
                                     "status_code": status.HTTP_202_ACCEPTED})

        # if serializer is invalid than return serializer.errors
        else:
            return Response({"success": False,
                             "message": f'Error! {serializer.errors}',
                             "status_code": status.HTTP_202_ACCEPTED},
                            status=status.HTTP_400_BAD_REQUEST)


class HarvestingEditAPIView(APIView):
    @swagger_auto_schema(request_body=HarvestingEditSerializer)
    @access_permission_required
    def put(self, request):
        print(f"Plain data: {request.data}")
        # check if harvesting_id is sent
        # if 'harvesting_id' not in request.data.keys() or request.data['harvesting_id'] is '':
        #     return Response({"success": False,
        #                      "message": 'harvest_id is required',
        #                      "status_code": status.HTTP_400_BAD_REQUEST},
        #                      status=status.HTTP_400_BAD_REQUEST)

        # check if harvesting_id is valid
        try:
            Harvesting.objects.get(id=request.data['harvesting_id'])
        except Harvesting.DoesNotExist:
            return Response({"success": False,
                             "message": 'Invalid harvesting_id',
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_404_NOT_FOUND)

        # check if harvest_quantity is integer or not
        try:
            int(request.data['quantity'])
        except ValueError:
            return Response({
                "success": False,
                "message": 'Invalid harvest quantity; it must be an integer',
                "status_code": status.HTTP_400_BAD_REQUEST},
                status=status.HTTP_400_BAD_REQUEST)

        serializer = HarvestingEditSerializer(data=request.data)

        if serializer.is_valid():
            try:
                plot_status = Plot.objects.get(id=request.data['plot_id']).status
                Harvesting.objects.filter(pk=request.data['harvesting_id']).update(
                    plot=request.data['plot_id'],
                    crop_status=request.data['crop_status'],
                    total_labor_hour=request.data['total_labor_hour'],
                    farmer=request.data['farmer'],
                    quantity=request.data['quantity'],
                    status=request.data['status'],
                    last_updated_by=request.data['user_id'],
                    sensor_data_N=request.data['sensor_data_N'],
                    sensor_data_P=request.data['sensor_data_P'],
                    sensor_data_K=request.data['sensor_data_K']
                )
            except Exception as e:
                return Response({
                    "success": False,
                    "message": f'Error {e}',
                    "status_code": status.HTTP_400_BAD_REQUEST
                }, status=status.HTTP_400_BAD_REQUEST)

        # update plot status based on updated harvest status
            harvest_status = request.data['status']
            print(f"Harvesting status: {harvest_status}")
            if harvest_status == "partially harvested":
                # update only plot status to "partially harvested"
                Plot.objects.filter(pk=request.data['plot_id']).update(status="partially harvested")
                # if active plot count is greater than 0 then update seeding & land status
                seeding_id = Plot.objects.get(pk=request.data['plot_id']).seeding.id  # get seeding id
                active_plot_count = Plot.objects.filter(seeding_id=seeding_id,
                                                        status__in=['ready', 'partially harvested']).count()
                if active_plot_count > 0:
                    seeding_obj = Seeding.objects.filter(pk=seeding_id)
                    seeding_obj.update(status="occupied")  # update seeding status
                    land_id = seeding_obj[0].land.id
                    Land.objects.filter(pk=land_id).update(status="occupied")
                    return Response({"success": True,
                                     "message": 'Harvest info updated successfully',
                                     "status_code": status.HTTP_202_ACCEPTED},
                                    status=status.HTTP_200_OK)
                else:
                    return Response({"success": False,
                                     "message": f'Error {serializer.errors}',
                                     "status_code": status.HTTP_400_BAD_REQUEST},
                                    status=status.HTTP_400_BAD_REQUEST)

            # update plot , seeding and land status (if fully harvested)
            elif harvest_status == "fully harvested":
                Plot.objects.filter(pk=request.data['plot_id']).update(status="fully harvested")
                # if active plot count is 0 then close the seeding and make the land free
                seeding_id = Plot.objects.get(pk=request.data['plot_id']).seeding.id  # get seeding id
                active_plot_count = Plot.objects.filter(seeding_id=seeding_id,
                                                        status__in=['ready', 'partially harvested']).count()
                if active_plot_count == 0:
                    seeding_obj = Seeding.objects.filter(pk=seeding_id)
                    seeding_obj.update(status="closed")  # update seeding status
                    land_id = seeding_obj[0].land.id
                    Land.objects.filter(pk=land_id).update(status="ready")
                    return Response({"success": True,
                                     "message": 'Harvest info updated successfully',
                                     "status_code": status.HTTP_202_ACCEPTED},
                                    status=status.HTTP_200_OK)
                else:
                    return Response({"success": False,
                                     "message": f'Error {serializer.errors}',
                                     "status_code": status.HTTP_400_BAD_REQUEST},
                                    status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"success": False,
                             "message": f'Error {serializer.errors}',
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)


class HarvestingListAPIView(APIView):
    @swagger_auto_schema(request_body=HarvestListSerializer)
    @access_permission_required
    def post(self, request):
        if 'plot_id' in request.data.keys():
            # get all harvest under the plot
            try:
                all_harvests = Harvesting.objects.filter(plot_id=request.data['plot_id'])
                serializer = HarvestingDetailSerializer(all_harvests, many=True)
                return Response({"success": True,
                                 "harvest_list": serializer.data,
                                 "status_code": status.HTTP_200_OK
                                 }, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response({"success": False,
                                 "message": f"Error! {e}",
                                 "status_code": status.HTTP_400_BAD_REQUEST
                                 }, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"success": False,
                             "message": f"plot_id is required",
                             "status_code": status.HTTP_400_BAD_REQUEST
                             }, status=status.HTTP_400_BAD_REQUEST)


class SeedingStatusAPIView(APIView):
    @swagger_auto_schema(request_body=SeedingStatusSerializer)
    # @access_permission_required
    def post(self, request):
        if 'seeding_id' in request.data.keys():

            try:
                with transaction.atomic():
                    seeding = Seeding.objects.filter(pk=request.data['seeding_id'])
                    land_id = seeding[0].land_id
                    # update seeding, land , plot status
                    seeding.update(status="damaged", last_updated_by=request.data['user_id'],
                                   last_updated_at=datetime.now())
                    Land.objects.filter(pk=land_id).\
                        update(status="ready", last_updated_by=request.data['user_id'],
                               last_updated_at=datetime.now())
                    Plot.objects.filter(seeding_id=request.data['seeding_id']).\
                        update(status="damaged",
                               last_updated_by=request.data['user_id'],
                               last_updated_at=datetime.now())

                    return Response({"success": True,
                                     "message": "Successfully Updated",
                                     "status_code": status.HTTP_200_OK
                                     }, status=status.HTTP_200_OK

                                    )

            except Exception as e:
                print(e)
                return Response({"success": False,
                                "message": f"Error {e}",
                                 "status_code": status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"success": False,
                             "message": "Please provide seeding_id",
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
