from django.urls import path
from accounts.views import get_statebycountry, get_country

urlpatterns = [
    path("get-country", get_country, name="get-country"),
    path("get-statebycountry", get_statebycountry, name="get-statebycountry"),
]
