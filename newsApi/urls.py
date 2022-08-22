"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    
"""

from django.urls import path
from .views.newsapi import NewsList

urlpatterns = [path("news-api", NewsList.as_view(), name="news-api")]
