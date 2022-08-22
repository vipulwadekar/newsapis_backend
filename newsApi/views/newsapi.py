from rest_framework.response import Response as DjangoRestResponse
from rest_framework import status
from rest_framework.views import APIView
from newsapi import NewsApiClient
import json
import pandas as pd
from newsApi.models.news import News
from newsApi.models.category import Category
from newsApi.serializers.news_serializers import NewsSerializer

# cabeda9386@zfobo.com
NEWSAPI_KEY = "1e2233fd441d4fb490a262bae9fa9f64"
# Init
newsapi = NewsApiClient(api_key=NEWSAPI_KEY)
# Create your views here.


class NewsList(APIView):
    """
    List all news, or create a new news.
    """

    def get(self, request, format=None):
        # taking i/p from params
        category = request.GET.get("category")
        country = request.GET.get("country")
        if category == None and country == None:
            return DjangoRestResponse(
                {"message": "Please provide category or country in query params"},
                status=status.HTTP_404_NOT_FOUND,
            )
        category_name = Category.objects.get(pk=1)
        # print(category_name.id)
        top_headlines = newsapi.get_top_headlines(country=country, category=category)
        # print("====================", (top_headlines["articles"]))
        top_headlines_articles_len = len(top_headlines["articles"])
        # news = top_headlines["articles"][0]
        print(top_headlines_articles_len)
        # for i in range(top_headlines_articles_len):
        #     # print(top_headlines["articles"][i]["author"])
        #     print("index", i)
        #     print(top_headlines["articles"][i]["title"])

        #     news_obj, news_created = News.objects.get_or_create(
        #         source_name=top_headlines["articles"][i]["source"]["name"],
        #         author=top_headlines["articles"][i]["author"],
        #         title=top_headlines["articles"][i]["title"],
        #         description=top_headlines["articles"][i]["description"],
        #         url=top_headlines["articles"][i]["url"],
        #         urlToImage=top_headlines["articles"][i]["urlToImage"],
        #         published_at=top_headlines["articles"][i]["publishedAt"],
        #         content=top_headlines["articles"][i]["content"],
        #         category=category_name,
        #     )
        #     print(type(news_obj))
        #     print(type(news_created))

        news_obj = News.objects.all()
        print(news_obj.count())
        serializer = NewsSerializer(news_obj, many=True)
        # for i in news:
        #     # print(key)1)status2)totalResults3)articles
        #     if i == "author":
        #         print("******************", news[i])

        # top_headlines_df = pd.DataFrame.from_dict(top_headlines)
        # json_obj = top_headlines_df.to_json(orient="records")

        return DjangoRestResponse(
            {
                "category": category,
                "country": country,
                "News Data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )
