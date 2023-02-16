from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    face_image = models.ImageField(upload_to='face_images/')
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.name
