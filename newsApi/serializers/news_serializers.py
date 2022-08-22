from rest_framework import serializers
from newsApi.models.news import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            "source_name",
            "author",
            "title",
            "description",
            "url",
            "urlToImage",
            "published_at",
            "content",
            "category",
        ]
