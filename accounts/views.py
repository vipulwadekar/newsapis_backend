from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response as DjangoRestResponse
from accounts.models import Country, State
from accounts.serializers import CountrySerializer
from accounts.serializers import StateSerializer
import json


@api_view(["GET"])
def get_country(request):

    country_obj = Country.objects.all()

    serializer = CountrySerializer(country_obj, many=True)
    return DjangoRestResponse(
        {
            "COUNTRY": serializer.data,
        },
        status=status.HTTP_201_CREATED,
    )


@api_view(["GET"])
def get_statebycountry(request):

    country = request.GET.get("country")
    print(country)
    if country == None:
        return DjangoRestResponse(
            {"message": "Please provide country in query params"},
            status=status.HTTP_404_NOT_FOUND,
        )
    country_name = Country.objects.get(name=country)

    print("DEBUG country_name: ", country_name)
    print("DEBUG country_id: ", country_name.id)

    state_obj = State.objects.all().filter(country=country_name)
    serializer = StateSerializer(state_obj, many=True)
    print("States", state_obj)
    return DjangoRestResponse(
        {
            str(country_name): serializer.data,
        },
        status=status.HTTP_201_CREATED,
    )
