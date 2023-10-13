from django.db import models


class Keyword(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)


class Trend(models.Model):
    name = models.CharField(max_length=100)
    result = models.IntegerField()
    search_period = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
