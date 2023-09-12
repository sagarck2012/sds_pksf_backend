from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from users.api.serializers import UserRegistrationSerializer, UserSerializer, LoginSerializer, UserRoleSerializer
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.conf import settings
from users.api import authentication
from rest_framework_jwt.settings import api_settings
from users.api.utils import generate_access_token
from users.models import User, Role, Privilege
from rest_framework import permissions
from rest_framework import exceptions
import jwt
from drf_yasg.utils import swagger_auto_schema
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token, ensure_csrf_cookie, csrf_protect
from users.decorators import access_permission_required
from django.db import connection
from processing.api.views import get_all
from .raw_sql_query import *
import json
from django.core.serializers.json import DjangoJSONEncoder


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'status_code': status.HTTP_201_CREATED,
            'message': 'User registered  successfully',
        }

        return Response(response, status=status.HTTP_201_CREATED)


class LoginView(RetrieveAPIView):

    def post(self, request):
        data = request.data
        email = data.get('email', '')
        password = data.get('password', '')
        # user = auth.authenticate(username=username, password=password)
        user = User.objects.get(email=email)

        if user:
            auth_token = jwt.encode(
                {'username': user.name}, api_settings.JWT_SECRET_KEY)

            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(method='post', request_body=LoginSerializer)
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    # print(request.headers)
    if 'email' not in request.data.keys() or request.data['email'] is '':
        raise exceptions.ValidationError({'success': False, 'message': 'email is required',
                                          'status_code': status.HTTP_400_BAD_REQUEST})
    if 'password' not in request.data.keys() or request.data['password'] is '':
        raise exceptions.ValidationError({'success': False, 'message': 'password is required',
                                          'status_code': status.HTTP_400_BAD_REQUEST})

    email = request.data.get('email')
    password = request.data.get('password')
    response = Response()
    user = User.objects.filter(email=email).first()

    if user is None:
        raise exceptions.AuthenticationFailed('user not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('wrong password')

    serialized_user = UserSerializer(user).data

    access_token = generate_access_token(user)
    # refresh_token = generate_refresh_token(user)

    # response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
    response.data = {
        'access_token': access_token,
        'user': serialized_user,
    }

    return response


class UserList(ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return User.objects.filter(email=self.request.user)


class UserProfileView(RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, **kwargs):
        try:
            user_profile = User.objects.get(user=request.user)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User profile fetched successfully',
                'data': [{
                    'first_name': user_profile.first_name,
                    'last_name': user_profile.last_name,
                    'phone_number': user_profile.phone_number,
                    'age': user_profile.age,
                    'gender': user_profile.gender,
                }]
            }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': False,
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User does not exist',
                'error': str(e)
            }
        return Response(response, status=status_code)


class UserEditAPIView(APIView):
    @swagger_auto_schema(request_body=UserSerializer)

    def put(self, request):
        # print(f"Sent data: {request.data}")
        if 'user_id' not in request.data.keys() or request.data['user_id'] is '':
            raise ValidationError({'message': 'user_id is required', 'status_code': status.HTTP_400_BAD_REQUEST})
        try:
            user = User.objects.get(id=request.data['user_id'])
            auth_user = authentication
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                # return Response(serializer.data)
                return Response({'message': 'user updated'}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserRoleListAPIView(APIView):
    # @access_permission_required
    def get(self, request):
        role_list = Role.objects.all()
        role_serializer = UserRoleSerializer(role_list, many=True)
        # print(f"Serializer : {role_serializer} and serialized data: {role_serializer.data}")
        # print(f"Serializer : {role_serializer}")
        # print(f"Serializer DATA: {role_serializer.data}")
        return Response(role_serializer.data)


class UserRolePrivilegeAPIView(APIView):
    # @access_permission_required
    def get(self, request):
        try:
            role_id = request.data['role_id']
        except KeyError:
            return Response({"message": "role_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        query = role_privilege(role_id)
        with connection.cursor() as cursor:
            cursor.execute(query)
            # get_all(cursor) converts query result from query set object to dictionary
            # to resolve date object is not json serializable issue cls=DjangoJSONEncoder is used
            query_result = json.loads(json.dumps(get_all(cursor), cls=DjangoJSONEncoder))
            return Response(query_result)


class UserRolePrivilegeUpdateAPIView(APIView):
    def post(self, request):
        received_data = request.data
        print(received_data)
        try:
            for data in received_data:
                Privilege.objects.filter(url=data['url_id']).update(is_allowed=data['is_allowed'])
        except Exception as e:
            print(e)
            return Response({"message": e}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "successfully updated"}, status=status.HTTP_202_ACCEPTED)

