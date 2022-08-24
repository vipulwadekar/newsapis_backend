from django.contrib import admin
from accounts.models import User, Country, State

# Register your models here.
admin.site.register([User, Country, State])
