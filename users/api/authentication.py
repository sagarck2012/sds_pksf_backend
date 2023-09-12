import jwt
from rest_framework.authentication import BaseAuthentication
from django.middleware.csrf import CsrfViewMiddleware
from rest_framework import exceptions, status
from django.conf import settings
from django.contrib.auth import get_user_model
from users.models import User


class SafeJWTAuthentication(BaseAuthentication):

    def authenticate(self, request):

        # User = get_user_model()
        authorization_header = request.headers.get('Authorization')

        if not authorization_header:
            return None
        try:
            # header = 'Token xxxxxxxxxxxxxxxxxxxxxxxx'
            access_token = authorization_header.split(' ')[1]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])

        except jwt.InvalidSignatureError:
            raise exceptions.AuthenticationFailed({'success': False, 'status_code': status.HTTP_403_FORBIDDEN, 'message': 'access_token invalid'})
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed({'success': False, 'status_code': status.HTTP_403_FORBIDDEN, 'message': 'access_token expired'})

        except IndexError:
            raise exceptions.AuthenticationFailed({'success': False, 'status_code': status.HTTP_403_FORBIDDEN, 'message': 'Token prefix missing'})

        user_id = payload.get('user_id')
        user = User.objects.filter(id=user_id).first()

        if user is None:
            raise exceptions.AuthenticationFailed({'success': False, 'status_code': status.HTTP_403_FORBIDDEN, 'message': 'User not found'})

        if not user.is_active:
            raise exceptions.AuthenticationFailed({'success': False, 'status_code': status.HTTP_403_FORBIDDEN, 'message': 'User inactive'})

        return (user, None)