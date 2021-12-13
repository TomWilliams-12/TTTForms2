from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager
from jsignature.fields import JSignatureField


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')

        return self.create_user(email, user_name, first_name, password, **other_fields)


class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    reg = models.CharField(max_length=10, blank=True, null=True)
    signature = JSignatureField(blank=True, null=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.first_name

