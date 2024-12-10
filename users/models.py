from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    objects = CustomUserManager()
    first_name = None
    last_name = None
    username = None
    USERNAME_FIELD = "email"
    email = models.EmailField("email", unique=True)
    name = models.CharField("name", max_length=150)
    cpf = models.CharField("cpf", max_length=15)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True, default='profile_pictures/default.jpg')
    REQUIRED_FIELDS = []
    
    def save(self, *args, **kwargs):
        if not self.profile_picture:
            self.profile_picture = 'profile_pictures/default.jpg'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
    

class Product(models.Model):
    pass
    
