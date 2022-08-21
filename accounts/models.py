from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from .manager import UserManager
# from accounts.models.role import Role
# Create your models here.
class User(AbstractUser):
    
    username = None
    email = models.EmailField(max_length=150, unique=True)
    is_deleted = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100,null=True,blank=True)
    last_login_time = models.DateTimeField(max_length=100,null=True,blank=True)
    last_logout_time = models.DateTimeField(max_length=100,null=True,blank=True)

    # role = models.ForeignKey(
    #     Role,
    #     on_delete=models.PROTECT,
    #     related_name='users',
    #     null=True,
    #     blank=True,
    # )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    users = UserManager()

    def __str__(self):
        return self.email