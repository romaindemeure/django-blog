from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, first_name=None, last_name=None, description=None):
        if not email:
            raise ValueError("Vous devez entrer un email.")

        user = self.model(
            email.self.normalize_email(email)
        )

        user.set_password(password)
        user.save()
        return self.create_user(email, password, first_name, last_name, description)

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255, blank=False)
    first_name = models.CharField(max_length=45, blank=False)
    last_name = models.CharField(max_length=45, blank=True)
    description = models.CharField(max_length=144, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]
    object = MyUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


