from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from .manager import UserManager


# from accounts.models.role import Role
# Create your models here.


class Country(models.Model):

    name = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class State(models.Model):

    name = models.CharField(max_length=256, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class User(AbstractUser):

    username = None
    email = models.EmailField(max_length=150, unique=True)
    is_deleted = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    last_login_time = models.DateTimeField(max_length=100, null=True, blank=True)
    last_logout_time = models.DateTimeField(max_length=100, null=True, blank=True)
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # state = models.ForeignKey(State, on_delete=models.CASCADE)
    # role = models.ForeignKey(
    #     Role,
    #     on_delete=models.PROTECT,
    #     related_name='users',
    #     null=True,
    #     blank=True,
    # )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    users = UserManager()

    def __str__(self):
        return self.email
