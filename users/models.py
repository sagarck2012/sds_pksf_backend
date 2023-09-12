from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from farm.models import ProductionHouse


class UserManager(BaseUserManager):
    '''
    creating a manager for a custom user model
    https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#writing-a-manager-for-a-custom-user-model
    https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#a-full-example
    '''
    def create_user(self, email,  role, name, address, phone_number, production_house, nid=None,  password=None,):
        """
        Create and return a `User` with an email, username and password.
        """
        if not email:
            raise ValueError('Users Must Have an email address')
        # if not role:
        #     raise ValueError('Users Must Have a role')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.role = role
        user.name = name
        user.address = address
        user.phone_number = phone_number
        user.nid = nid
        user.production_house = production_house
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class Role(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100)
    last_updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_updated_by = models.CharField(max_length=100)

    # ...
    def __str__(self):
        return self.name


class User(AbstractBaseUser):
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    nid = models.CharField(max_length=12, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=11, unique=True)
    photo = models.ImageField(upload_to='images/users/', height_field=None, width_field=None, max_length=100,
                              blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    production_house = models.ForeignKey(ProductionHouse, on_delete=models.CASCADE)
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100)
    last_updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_updated_by = models.CharField(max_length=100)
    last_login = models.DateTimeField(null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    # ...
    def __str__(self):
        return f"{self.email}"


class Menu_name(models.Model):
    name = models.CharField(max_length=300, null=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    created_date = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)
    updated_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'i_menu_name'


class Module_name(models.Model):
    menuname = models.ForeignKey(Menu_name, on_delete=models.CASCADE, null=True, blank=True)
    modulename = models.CharField(max_length=300, null=True, blank=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    created_date = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)
    updated_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.modulename}"

    class Meta:
        db_table = 'i_module_name'


class Module_action(models.Model):
    menuname = models.ForeignKey(Menu_name, on_delete=models.CASCADE, null=True, blank=True)
    modulename = models.ForeignKey(Module_name, on_delete=models.CASCADE)
    url = models.CharField(max_length=300, null=True, blank=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    created_date = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)
    updated_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.url}"

    class Meta:
        db_table = 'i_module_action'


class Privilege(models.Model):
    menuname = models.ForeignKey(Menu_name, on_delete=models.CASCADE, null=True, blank=True)
    modulename = models.ForeignKey(Module_name, on_delete=models.CASCADE)
    url = models.ForeignKey(Module_action, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    role_type = models.IntegerField(default=0)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    created_date = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    is_allowed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.menuname}"

    class Meta:
        db_table = 'i_privilege'