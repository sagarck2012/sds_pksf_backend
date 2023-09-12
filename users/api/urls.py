from django.urls import path
from .views import UserRegistrationView, LoginView, UserList, login_view, UserProfileView, UserEditAPIView, \
    UserRoleListAPIView, UserRolePrivilegeAPIView, UserRolePrivilegeUpdateAPIView


urlpatterns = [
    path('user/register/', UserRegistrationView.as_view(), name='user_register'),
    path('user/login/', login_view, name='user_login'),
    path('user/profile/', UserProfileView.as_view(), name='user_profile'),
    path('user/edit/', UserEditAPIView.as_view(), name='user_edit'),
    path('user/role_list/', UserRoleListAPIView.as_view(), name='user_role_list'),
    path('user/role_privilege/', UserRolePrivilegeAPIView.as_view(), name='user_role_privilege'),
    path('user/role_privilege_update/', UserRolePrivilegeUpdateAPIView.as_view(), name='user_role_privilege_update'),
]