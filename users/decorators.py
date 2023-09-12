from users.models import *
from django.urls import resolve
from rest_framework.response import Response
from rest_framework import status


def access_permission_required(function):
    def wrapper(self, request, *args, **kwargs):
        try:
            user_id = request.data['user_id']
        except KeyError:
            return Response({"message": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        url = resolve(request.get_full_path()).route
        # print(f"url: {url} is requested from user_id: {user_id}")
        try:
            user_role_id = User.objects.get(pk=user_id).role
            url_id = Module_action.objects.get(url=url).id
            privileged = Privilege.objects.get(role=user_role_id, url=url_id).is_allowed
        except Exception as e:
            print(e)
            privileged = False

        if privileged is False:
            return Response({"message": "Access Denied!"}, status=status.HTTP_403_FORBIDDEN)
        else:
            return function(self, request, *args, **kwargs)

    return wrapper
