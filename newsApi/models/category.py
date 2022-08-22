from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)

    def __str__(self):
        return f"{self.name}"
