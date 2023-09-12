import datetime
import jwt
from django.conf import settings
from django.utils import timezone
from datetime import datetime
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from users.models import User


def generate_access_token(user):
    # print(f"user_id: {user.id},iat: {datetime.now()}, exp: {datetime.now() + settings.JWT_TIMEOUT}")
    access_token_payload = {
        'user_id': user.id,
        'exp': datetime.now() + settings.JWT_TIMEOUT,
        'iat': datetime.now()
    }
    access_token = jwt.encode(access_token_payload,
                              settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
    return access_token


