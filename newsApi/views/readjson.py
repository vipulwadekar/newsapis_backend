from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response as DjangoRestResponse
import json


@api_view(["GET"])
def read_json(request):

    json_data = open("newsApi/views/Countries.json")
    data1 = json.load(json_data)  # deserialises it
    print("debug : ", type(data1))
    json_data.close()
    return DjangoRestResponse(
        {
            "Newsdata": data1,
        },
        status=status.HTTP_201_CREATED,
    )
