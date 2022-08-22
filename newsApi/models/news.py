from django.db import models

from newsApi.models.category import Category

# import uuid

# Create your models here
class News(models.Model):
    # source_id = models.UUIDField(default=uuid.uuid4, unique=True)
    source_name = models.CharField(max_length=256, blank=True, null=True)
    author = models.CharField(max_length=256, blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    url = models.CharField(max_length=256, blank=True, null=True)
    urlToImage = models.CharField(max_length=256, blank=True, null=True)
    published_at = models.CharField(max_length=256, blank=True, null=True)
    content = models.CharField(max_length=256, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.author}"


"""
"source": {
        "id": "the-washington-post",
        "name": "The Washington Post"
    },
    "author": "Joe McDonald | AP",
    "title": "Asian stocks mixed before Fed meeting after China cuts rate - The Washington Post",
    "description": "Asian stock markets are mixed after China cut an interest rate that affects mortgage costs",
    "url": "https://www.washingtonpost.com/business/asian-stocks-mixed-before-fed-meeting-after-china-cuts-rate/2022/08/22/74c5f154-21d3-11ed-a72f-1e7149072fbc_story.html",
    "urlToImage": "https://www.washingtonpost.com/wp-apps/imrs.php?src=https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/XCPH4VRB2II63JZPDZYUSBZPXQ.jpg&w=1440",
    "publishedAt": "2022-08-22T04:32:57Z",
    "content": "Comment on this story\r\nBEIJING Asian stock markets were mixed Monday after China cut an interest rate that affects mortgage lending while investors looked ahead to this weeks Federal Reserve conferen… [+3156 chars]"
"""
