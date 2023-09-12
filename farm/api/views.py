# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import status
from rest_framework.validators import ValidationError
from .serializer import FarmerSerializer, DivisionSerializer, DistrictSerializer, \
    UpazilaSerializer, OwnerSerializer, LandSerializer, CropSerializer, VegetableSerializer,\
    VegetableVariantSerializer, CropTypeSerializer, DistrictSearchSerializer, ProductionHouseSerializer, \
    FarmerIdSerializer, OwnerIdSerializer, LandIdSerializer, UserIdSerializer, FarmerEditSerializer, \
    OwnerEditSerializer, LandEditSerializer, CropTypeSearchSerializer, CropVariantSearchSerializer, LandListSerializer
from farm.models import Farmer, Division, District, Upazila, Owner, Land, Crop, CropType, Vegetable, ProductionHouse
from users.models import User
# import base64
# Create your views here.
from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
from users.models import *
from users.decorators import access_permission_required
from django.core.exceptions import ObjectDoesNotExist


class FarmerListAPIView(APIView):
    @swagger_auto_schema(request_body=UserIdSerializer)
    @access_permission_required
    def post(self, request):
        print(f"request.headers:{request.headers}")
        farmers = Farmer.objects.filter(delete_status=0)  # only active farmers
        print(f"farmers: {farmers}")
        serializer = FarmerSerializer(farmers, many=True)
        # print(f"Photo field: {serializer.data.photo}")
        print(f"Serializer : {serializer}")
        return Response({"success": True,
                         "farmer_list": serializer.data,
                         "status_code": status.HTTP_200_OK
                         },
                        status=status.HTTP_200_OK)


# class FarmerAPIView(APIView):
#
#
#
#     def post(self, request):
#         print(f"Received JSON: {request.data}")
#         print(f"base64 image: {request.data['photo']}")
#         #
#         # request.data["photo"] = base64.b64decode(request.data["photo"])
#         # request.data["photo"] = bytes(request.data["photo"], 'utf-8')
#         # print(f"Binary photo: {request.data['photo']}")
#         # print(f"request.data: {request.data}")
#         # print(f"request.data: {request.data}")
#         # test_string = "test string"
#         # res = bytes(test_string, 'utf-8')
#         # request.data["photo"] = res
#         print(f"request.data: {request.data}")
#         serializer = FarmerSerializer(data=request.data)
#         if serializer.is_valid():
#             farmer_data = serializer.save()
#             if 'photo' in request.data.keys():
#                 farmer_data.photo = bytes(request.data['photo'], 'utf-8')
#                 farmer_data.save()
#         # save_obj = Farmer.objects.create(
#         #     photo=request.data['photo'],
#         #     total_land=2
#         # )
#         # save_obj.save()
#             return Response(serializer.data)
#         return Response(request.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FarmerAddAPIView(APIView):
    @swagger_auto_schema(request_body=FarmerSerializer)
    @access_permission_required
    def post(self, request):

        # print(f"Before update: {request.data}")
        # request.data.update({'new_key': "new_value"})
        # print(f"After update: {request.data}")
        user_id = request.data['user_id']
        del request.data['user_id']  # removed user_id after access permission check to get through serializer.valid()
        serializer = FarmerSerializer(data=request.data)
        # serializer = FarmerSerializer()
        if serializer.is_valid():
            # farmer_data = serializer.save()
            # if 'photo' in request.data.keys():
            #     farmer_data.photo = bytes(request.data['photo'], 'utf-8')
            #     farmer_data.save()
            serializer.save(created_by=user_id, last_updated_by=user_id)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({
                "success": True,
                "message": 'Farmer Added Successfully',
                "status_code": status.HTTP_201_CREATED},
                status=status.HTTP_201_CREATED)
        else:
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"success": False,
                            "message": f'Error {serializer.errors}',
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)


# class FarmerDetails(APIView):
#
#     def get_object(self, id):
#         try:
#             return Farmer.objects.get(id=id)
#         except Farmer.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request):
#         farmer = self.get_object(request.data['id'])
#         print(f"Farmer Name: {farmer.name}")
#
#         serializer = FarmerSerializer(farmer)
#         print(f"Serialized data: {serializer.data}")
#         if serializer.data['photo'] is not None:
#             serializer.data['photo'] = serializer.data['photo'].decode('utf-8')
#         # print(f"Serializser: {serializer.data}")
#         print(f"Serializer: {serializer}")
#         return Response(serializer.data)
#
#     def put(self, request):
#         # print(f"Sent data: {request.data}")
#         farmer = self.get_object(request.data['id'])
#         serializer = FarmerSerializer(farmer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     # def delete(self, request, id):
#     #     farmer = self.get_object(id)
#     #     farmer.delete()
#     #     return Response(status=status.HTTP_204_NO_CONTENT)


# def convert_to_binary(filename):
#     # Convert digital data to binary format
#     with open(filename, 'rb') as file:
#         binary_data = file.read()
#     return binary_data


class FarmerEditAPIView(APIView):
    @swagger_auto_schema(request_body=FarmerEditSerializer)
    @access_permission_required
    def put(self, request):
        # print(f"Sent data: {request.data}")
        if 'farmer_id' not in request.data.keys() or request.data['farmer_id'] is '':
            # raise ValidationError({'message': 'owner_id is required', 'status_code': '400'})
            return Response({"success": False,
                            "message": 'Valid farmer_id is required',
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            # farmer = self.get_object(request.data['farmer_id'])
            farmer = Farmer.objects.get(id=request.data['farmer_id'], delete_status=0)
            serializer = FarmerSerializer(farmer, data=request.data)
            if serializer.is_valid():
                serializer.save(last_updated_by=request.data['user_id'])
                # return Response(serializer.data)
                return Response({"success": True,
                                "message": 'Farmer updated successfully',
                                 "status_code": status.HTTP_202_ACCEPTED},
                                status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"success": False,
                                "message": f'Error {serializer.errors}',
                                 "status_code": status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)
        except Farmer.DoesNotExist:
            return Response({"success": False,
                            "message": 'Invalid farmer_id',
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_404_NOT_FOUND)


class FarmerSearchAPIView(APIView):

    # def get_object(self, id):
    #     try:
    #         return Farmer.objects.get(id=id)
    #     except Farmer.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    # @swagger_auto_schema(manual_parameters=[farmer_id])
    # @swagger_auto_schema()
    @swagger_auto_schema(request_body=FarmerIdSerializer)
    @access_permission_required
    def post(self, request):
        # print(f"Sent data: {request.data}")
        if 'farmer_id' not in request.data.keys() or request.data['farmer_id'] is '':
            # raise ValidationError({'message': 'owner_id is required', 'status_code': '400'})
            return Response({"success": False,
                             "message": 'farmer_id is required',
                             "status_code": status.HTTP_404_NOT_FOUND},
                            status=status.HTTP_404_NOT_FOUND)
        try:
            farmer = Farmer.objects.get(id=request.data['farmer_id'], delete_status=0)
            serializer = FarmerSerializer(farmer, many=False)
        # print(f"Search data: {serializer.data.pop('photo')} & type: "
        #       f"{type(serializer.data.pop('photo'))}")
        # print(f"decoded data: {serializer.data.pop('photo').decode('ascii') }")
        # print(f"photo: {serializer.data['photo']} & type: {type(serializer.data['photo'])}")
            return Response({"success": True,
                             "farmer_info": serializer.data,
                             "status_code": status.HTTP_200_OK},
                            status=status.HTTP_200_OK)
        except Farmer.DoesNotExist:
            return Response({"success": False,
                             "message": 'Invalid farmer_id',
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)


class FarmerDeleteAPIView(APIView):

    # def get_object(self, id):
    #     try:
    #         return Farmer.objects.get(id=id)
    #     except Farmer.DoesNotExist:
    #         return Response({"success": False,
    #                          "message": 'Invalid farmer_id',
    #                          "status_code": status.HTTP_404_NOT_FOUND},
    #                         status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=FarmerIdSerializer)
    @access_permission_required
    def post(self, request):
        # print(f"Sent data: {request.data}")
        try:
            farmer = Farmer.objects.get(pk=request.data['farmer_id'], delete_status=0)
            farmer.delete_status = 1
            farmer.last_updated_by = request.data['user_id']
            farmer.save()
            return Response({"success": True,
                             "message": 'Farmer removed successfully',
                             "status_code": status.HTTP_202_ACCEPTED},
                            status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            print(e)
            return Response({"success": False,
                             "message": 'Invalid farmer_id',
                             "status_code": status.HTTP_404_NOT_FOUND
                             },
                            status=status.HTTP_404_NOT_FOUND)


class DivisionAPIView(APIView):
    @swagger_auto_schema(request_body=UserIdSerializer)
    @access_permission_required
    def post(self, request):
        if 'division_id' in request.data.keys():
            try:
                division = Division.objects.get(pk=request.data['division_id'])
            except Division.DoesNotExist:
                return Response({"success": False,
                                 "message": 'Invalid division_id',
                                 "status_code": status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_404_NOT_FOUND)

            serializer = DivisionSerializer(division, many=False)
            # return Response(serializer.data)
            return Response({"success": True,
                             "division_list": serializer.data,
                             "status_code": status.HTTP_200_OK
                             }, status=status.HTTP_200_OK)
        else:
            division = Division.objects.all()
            serializer = DivisionSerializer(division, many=True)
            print(f"Serializer : {serializer}")
            return Response({"success": True,
                             "division_list": serializer.data,
                             "status_code": status.HTTP_200_OK
                             }, status=status.HTTP_200_OK)


class DistrictAPIView(APIView):
    @swagger_auto_schema(request_body=UserIdSerializer)
    @access_permission_required
    def post(self, request):
        # print(f"request.data : {request.data}")
        if 'district_id' in request.data.keys():
            try:
                district = District.objects.get(pk=request.data['district_id'])
            except District.DoesNotExist:
                return Response({"success": False,
                                 "message": 'Invalid district_id',
                                 "status_code": status.HTTP_404_NOT_FOUND},
                                status=status.HTTP_404_NOT_FOUND)

            serializer = DistrictSerializer(district, many=False)
        elif 'division_id' in request.data.keys():
            district = District.objects.filter(division=request.data['division_id'])
            serializer = DistrictSerializer(district, many=True)
        else:
            district = District.objects.all()
            serializer = DistrictSerializer(district, many=True)
        print(f"Serializer : {serializer}")
        # return Response(serializer.data)

        return Response({"success": True,
                         "district_list": serializer.data,
                         "status_code": status.HTTP_200_OK
                         },
                        status=status.HTTP_200_OK)


class UpazilaAPIView(APIView):
    # @swagger_auto_schema(request_body=UpazilaSearchSerializer)
    # @swagger_auto_schema(responses={200: UpazilaSerializer(many=True)})
    # @swagger_auto_schema(manual_parameters=[
        # openapi.Parameter('test', openapi.IN_QUERY, "test manual param", type=openapi.TYPE_BOOLEAN),
        # openapi.Parameter('district_id', openapi.IN_BODY, "upz of district", type=openapi.TYPE_NUMBER),
    # ])
    @swagger_auto_schema(request_body=UserIdSerializer)
    @access_permission_required
    def post(self, request):
        if 'upazila_id' in request.data.keys():
            try:
                upazila = Upazila.objects.get(pk=request.data['upazila_id'])
            except District.DoesNotExist:
                return Response({"success": False,
                                 "message": 'Invalid upazila_id',
                                 "status_code": status.HTTP_404_NOT_FOUND},
                                status=status.HTTP_404_NOT_FOUND)

            serializer = UpazilaSerializer(upazila, many=False)
        elif 'district_id' in request.data.keys():
            print(f"district_id {request.data['district_id']}")
            upazila = Upazila.objects.filter(district=request.data['district_id'])
            serializer = UpazilaSerializer(upazila, many=True)
        else:
            upazila = Upazila.objects.all()
            serializer = UpazilaSerializer(upazila, many=True)
        print(f"Serializer : {serializer}")
        # return Response(serializer.data)
        return Response({"success": True,
                         "upazilla_list": serializer.data,
                         "status_code": status.HTTP_200_OK},
                        status=status.HTTP_200_OK)


class OwnerListAPIView(APIView):
    def get(self, request):
        owners = Owner.objects.filter(delete_status=0)  # only active farmers
        serializer = OwnerSerializer(owners, many=True)
        # print(f"Photo field: {serializer.data.photo}")
        print(f"Serializer : {serializer}")
        return Response(serializer.data)


class OwnerAddAPIView(APIView):
    @swagger_auto_schema(request_body=OwnerSerializer)
    @access_permission_required
    def post(self, request):
        user_id = request.data['user_id']
        del request.data['user_id']  # removed user_id after access permission check to get through serializer.valid()
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=user_id, last_updated_by=user_id)
            # return Response(request.data, status=status.HTTP_201_CREATED)
            return Response({"success": True,
                             "message": 'Owner added successfully',
                             "status_code": status.HTTP_201_CREATED},
                            status=status.HTTP_201_CREATED)
        else:
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"success": False,
                            "message": serializer.errors,
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)


class OwnerListAPIView(APIView):
    @swagger_auto_schema(request_body=UserIdSerializer)
    @access_permission_required
    def post(self, request):
        owners = Owner.objects.filter(delete_status=0)  # only active farmers
        serializer = OwnerSerializer(owners, many=True)
        # print(f"Serializer : {serializer}")
        # return Response(serializer.data)
        return Response({"success": True,
                         "owner_list": serializer.data,
                         "status_code": status.HTTP_200_OK},
                        status=status.HTTP_200_OK)


class OwnerSearchAPIView(APIView):
    @swagger_auto_schema(request_body=OwnerIdSerializer)
    @access_permission_required
    def post(self, request):

        if 'owner_id' not in request.data.keys() or request.data['owner_id'] is '':
            # raise ValidationError({'message': 'owner_id is required', 'status_code': '400'})
            # return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response({"success": False,
                             "message": 'Invalid owner_id',
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            owner = Owner.objects.get(id=request.data['owner_id'], delete_status=0)
            serializer = OwnerSerializer(owner, many=False)
            return Response({"success": True,
                             "owner_list": serializer.data,
                             "status_code": status.HTTP_200_OK},
                            status=status.HTTP_200_OK)

        except Owner.DoesNotExist:
            return Response({"success": False,
                             "message": 'Invalid owner_id',
                             "status_code": status.HTTP_404_NOT_FOUND},
                            status=status.HTTP_404_NOT_FOUND)


class OwnerEditAPIView(APIView):
    @swagger_auto_schema(request_body=OwnerEditSerializer)
    @access_permission_required
    def put(self, request):
        if 'owner_id' not in request.data.keys() or request.data['owner_id'] is '':
            # raise ValidationError({'message': 'owner_id is required', 'status_code': '400'})
            # return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response({"success": False,
                             "message": 'Invalid owner_id',
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            owner = Owner.objects.get(id=request.data['owner_id'], delete_status=0)
        except Owner.DoesNotExist:
            return Response({"success": False,
                             "message": 'Invalid owner_id',
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = OwnerSerializer(owner, data=request.data)
        if serializer.is_valid():
            serializer.save(last_updated_by=request.data['user_id'])
            # return Response(serializer.data)
            return Response({"success": True,
                             "message": 'Owner updated successfully',
                             "status_code": status.HTTP_202_ACCEPTED},
                            status=status.HTTP_202_ACCEPTED)
        else:
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"success": False,
                             "message": serializer.errors,
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)


class OwnerDeleteAPIView(APIView):
    @swagger_auto_schema(request_body=OwnerIdSerializer)
    @access_permission_required
    def post(self, request):
        if 'owner_id' not in request.data.keys() or request.data['owner_id'] is '':
            # return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response({"success": False,
                             "message": 'Invalid owner_id',
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            owner = Owner.objects.get(id=request.data['owner_id'], delete_status=0)
        except Owner.DoesNotExist:
            return Response({"success": False,
                             "message": 'Invalid owner_id',
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)

        owner.delete_status = 1
        owner.last_updated_by = request.data['user_id']
        owner.save()
        return Response({"success": True,
                         "message": 'Owner removed successfully',
                         "status_code": status.HTTP_202_ACCEPTED},
                        status=status.HTTP_202_ACCEPTED)


class LandAddAPIView(APIView):
    @swagger_auto_schema(request_body=LandSerializer)
    @access_permission_required
    def post(self, request):
        # print(f"received data: {request.data} & type: {type(request.data)}")
        if 'area_unit' in request.data.keys() and request.data['area_unit'] != '':
            if request.data['area_unit'] == 'sq-ft':
                request.data['area'] = request.data['area'] * 0.092903  # converting to sq-m
            if request.data['area_unit'] == "acre":
                request.data['area'] = request.data['area'] * 4046.86  # converting to sq-m

        else:
            # return Response({"message": "Invalid area unit"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"success": False,
                             "message": 'Invalid area unit',
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
        # request.data["status"] = "ready"
        # request.data["is_active"] = 1
        user_id = request.data['user_id']
        del request.data['user_id']  # removed user_id after access permission check to get through serializer.valid()
        del request.data['area_unit']  # removed area_unit after unit converted to sq-m
        serializer = LandSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            serializer.save(created_by=user_id, last_updated_by=user_id, status="ready", is_active=1)
            # return Response(request.data, status=status.HTTP_201_CREATED)

            return Response({"success": True,
                             "message": 'Land added successfully',
                             "status_code": status.HTTP_201_CREATED},
                            status=status.HTTP_201_CREATED)
        else:
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"success": False,
                             "message": serializer.errors,
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)


class LandListAPIView(APIView):

    @swagger_auto_schema(request_body=UserIdSerializer)
    @access_permission_required
    def post(self, request):
        lands = Land.objects.filter(is_active=1)  # only active land
        serializer = LandListSerializer(lands, many=True)

        # print(f"Serializer : {serializer}")
        # return Response(serializer.data)
        return Response({"success": True,
                         "land_list": serializer.data,
                         "status_code": status.HTTP_200_OK},
                        status=status.HTTP_200_OK)


class LandSearchAPIView(APIView):
    @swagger_auto_schema(request_body=LandIdSerializer)
    @access_permission_required
    def post(self, request):

        if 'land_id' not in request.data.keys() or request.data['land_id'] is '':
            # raise ValidationError({'message': 'owner_id is required', 'status_code': '400'})
            return Response({"success": False,
                             "message": "Invalid land_id",
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            land = Land.objects.get(id=request.data['land_id'], is_active=1)
            serializer = LandSerializer(land, many=False)
            # return Response(serializer.data)
            return Response({"success": True,
                             "land_list": serializer.data,
                             "status_code": status.HTTP_200_OK},
                            status=status.HTTP_200_OK)

        except Land.DoesNotExist:
            return Response({"success": False,
                             "message": 'Invalid land_id',
                             "status_code": status.HTTP_404_NOT_FOUND},
                            status=status.HTTP_404_NOT_FOUND)


class LandDeleteAPIView(APIView):
    @swagger_auto_schema(request_body=LandIdSerializer)
    @access_permission_required
    def put(self, request):
        if 'land_id' not in request.data.keys() or request.data['land_id'] is '':
            return Response({"success": False,
                             "message": "Invalid land_id",
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            land = Land.objects.get(id=request.data['land_id'], is_active=1)
        except Land.DoesNotExist:
            return Response({"success": False,
                             "message": 'Invalid land_id',
                             "status_code": status.HTTP_404_NOT_FOUND},
                            status=status.HTTP_404_NOT_FOUND)

        land.is_active = 0
        land.save(last_updated_by=request.data['user_id'])
        return Response(status=status.HTTP_202_ACCEPTED)


class LandEditAPIView(APIView):
    @swagger_auto_schema(request_body=LandEditSerializer)
    @access_permission_required
    def put(self, request):
        # print(f"Plain area: {request.data['area']}")
        if 'land_id' not in request.data.keys() or request.data['land_id'] is '':
            # raise ValidationError({'message': 'owner_id is required', 'status_code': '400'})
            # return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response({"success": False,
                             "message": "Invalid land_id",
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            land = Land.objects.get(id=request.data['land_id'], is_active=1)
        except Land.DoesNotExist:
            return Response({"success": False,
                             "message": "Invalid land_id",
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)

        if 'area_unit' in request.data.keys() and request.data['area_unit'] != '':
            if request.data['area_unit'] == 'sq-ft':
                request.data['area'] = request.data['area'] * 0.092903
            if request.data['area_unit'] == "acre":
                request.data['area'] = request.data['area'] * 4046.86

            # print(f"Updated area: {request.data['area']}")
            serializer = LandSerializer(land, data=request.data)
            if serializer.is_valid():
                serializer.save(last_updated_by=request.data['user_id'])
                # return Response(serializer.data)
                return Response({"success": True,
                                 "message": 'Land updated successfully',
                                 "status_code": status.HTTP_202_ACCEPTED},
                                status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"success": False,
                                 "message": serializer.errors,
                                 "status_code": status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"success": False,
                             "message": "Invalid area unit",
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)


class DistrictSearchAPIView(APIView):
    @access_permission_required
    @swagger_auto_schema(request_body=DistrictSearchSerializer)
    # @swagger_auto_schema(request_body=)
    def post(self, request):
        if 'district_id' in request.data.keys():
            try:
                district = District.objects.get(pk=request.data['district_id'])
            except District.DoesNotExist:
                return Response({"success": False,
                                 "message": 'Invalid district_id',
                                 "status_code": status.HTTP_404_NOT_FOUND},
                                status=status.HTTP_404_NOT_FOUND)

            serializer = DistrictSerializer(district, many=False)
            # return Response(serializer.data)

            return Response({"success": True,
                             "district_list": serializer.data,
                             "status_code": status.HTTP_200_OK},
                            status=status.HTTP_200_OK)
        elif 'division_id' in request.data.keys():
            district = District.objects.filter(division=request.data['division_id'])
            serializer = DistrictSerializer(district, many=True)
            # return Response(serializer.data)
            return Response({"success": True,
                             "district_list": serializer.data,
                             "status_code": status.HTTP_200_OK},
                            status=status.HTTP_200_OK)

        else:
            # return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response({"success": False,
                             "message": 'Invalid division_id/district_id',
                             "status_code": status.HTTP_404_NOT_FOUND},
                            status=status.HTTP_404_NOT_FOUND)


class CropListAPIView(APIView):
    @swagger_auto_schema(request_body=UserIdSerializer)
    @access_permission_required
    def post(self, request):
        crop = Crop.objects.filter(delete_status=0)  # only active crop
        serializer = CropSerializer(crop, many=True)
        # print(f'serializer: {serializer}')
        # return Response(serializer.data)
        return Response({"success": True,
                         "crop_list": serializer.data,
                         "status_code": status.HTTP_200_OK},
                        status=status.HTTP_200_OK)


class CropTypeListAPIView(APIView):
    @swagger_auto_schema(request_body=CropTypeSearchSerializer)
    @access_permission_required
    def post(self, request):
        crop_id = request.data['crop_id']
        vegetable = CropType.objects.filter(crop_id=crop_id, delete_status=0)  # crop_id 5 for vegetable
        serializer = VegetableSerializer(vegetable, many=True)
        # serializer = CropTypeSerializer(vegetable, many=True)
        # return Response(serializer.data)
        return Response({"success": True,
                         "crop_type_list": serializer.data,
                         "status_code": status.HTTP_200_OK},
                        status=status.HTTP_200_OK)


class CropTypeAddAPIView(CreateAPIView):
    serializer_class = CropTypeSerializer

    def post(self, request, *args, **kwargs):
        if 'crop_category_id' not in request.data.keys() or request.data['crop_category_id'] is '':
            raise ValidationError({'message': 'crop_category_id is needed', 'status_code': status.HTTP_400_BAD_REQUEST, "success": False})
        if 'local_name' not in request.data.keys() or request.data['local_name'] is '':
            raise ValidationError({'message': 'local_name is needed', 'status_code': status.HTTP_400_BAD_REQUEST, "success": False})
        if 'eng_name' not in request.data.keys() or request.data['eng_name'] is '':
            raise ValidationError({'message': 'eng_name is needed', 'status_code': status.HTTP_400_BAD_REQUEST, "success": False})

        crop_category_id = request.data.get('crop_category_id')
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(crop_id=crop_category_id)
            return Response({'success': True, 'status_code': status.HTTP_201_CREATED, 'message': 'crop_type added'}, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CropTypeEditAPIView(UpdateAPIView):
    serializer_class = CropTypeSerializer

    @access_permission_required
    def put(self, request, *args, **kwargs):
        if 'crop_type_id' not in request.data.keys() or request.data['crop_type_id'] is '':
            raise ValidationError(
                {'message': 'crop_type_id is needed', 'status_code': status.HTTP_400_BAD_REQUEST, "success": False})

        crop_type = CropType.objects.get(id=request.data['crop_type_id'])
        serializer = self.serializer_class(crop_type, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'status_code': status.HTTP_202_ACCEPTED, 'message': 'crop_type updated'},
                        status=status.HTTP_202_ACCEPTED)


class CropTypeDeleteAPIView(DestroyAPIView):
    @access_permission_required
    def delete(self, request, *args, **kwargs):
        if 'crop_type_id' not in request.data.keys() or request.data['crop_type_id'] is '':
            raise ValidationError(
                {'message': 'crop_type_id is needed', 'status_code': status.HTTP_400_BAD_REQUEST, "success": False})

        crop_type_id = request.data.get('crop_type_id')
        crop_type = CropType.objects.get(id=crop_type_id)
        crop_type.delete_status = 1
        crop_type.save()
        return Response({'success': True, 'status_code': status.HTTP_202_ACCEPTED, 'message': 'crop_type deleted'},
                        status=status.HTTP_202_ACCEPTED)


class CropVariantAPIView(APIView):
    @swagger_auto_schema(request_body=CropVariantSearchSerializer)
    @access_permission_required
    def post(self, request):
        if 'crop_type_id' not in request.data.keys() or request.data['crop_type_id'] is '':
            # raise ValidationError({'success': False, 'message': 'crop_type_id is required', 'status_code': status.HTTP_400_BAD_REQUEST})
            return Response({"success": False,
                             "message": 'crop_type_id is required',
                             "status_code": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)

        crop_type_id = request.data.get('crop_type_id')
        variant = Vegetable.objects.filter(vegetable_type_id=crop_type_id, delete_status=0)  # crop_id 5 for vegetable
        serializer = VegetableVariantSerializer(variant, many=True)
        return Response({"success": True,
                         "land_list": serializer.data,
                         "status_code": status.HTTP_200_OK},
                        status=status.HTTP_200_OK)


class VegetableVariantAddAPIView(CreateAPIView):
    serializer_class = VegetableVariantSerializer

    @access_permission_required
    def post(self, request):
        if 'crop_type_id' not in request.data.keys() or request.data['crop_type_id'] is '':
            raise ValidationError({'success': False, 'message': 'crop_type_id is required',
                                   'status_code': status.HTTP_400_BAD_REQUEST})

        crop_type_id = request.data.pop('crop_type_id')
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(vegetable_type_id=crop_type_id)
        return Response({'success': True, 'status_code': status.HTTP_201_CREATED, 'message': 'variant added'},
                        status=status.HTTP_201_CREATED)


class ProductionHouseListAPIView(APIView):
    @swagger_auto_schema(request_body=UserIdSerializer)
    @access_permission_required
    def post(self, request):
        if 'user_id' not in request.data.keys() or request.data['user_id'] is '':
            raise ValidationError({'success': False, 'message': 'user_id is required', 'status_code': status.HTTP_400_BAD_REQUEST})

        user_id = request.data['user_id']

        try:
            user = User.objects.get(id=user_id, is_active=1)
            prod_house = ProductionHouse.objects.filter(id=user.production_house_id)
        except (ObjectDoesNotExist, User.MultipleObjectsReturned):
            return Response({'message': 'user inactive or doesnt exist', 'success': False, 'status_code': status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)


        serializer = ProductionHouseSerializer(prod_house, many=True)
        return Response({"success": True,
                         "production_house_list": serializer.data,
                         "status_code": status.HTTP_200_OK},
                        status=status.HTTP_200_OK)




