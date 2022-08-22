from django.contrib import admin
from .models.category import Category
from .models.news import News

# Register your models here.
admin.site.register([Category, News])
