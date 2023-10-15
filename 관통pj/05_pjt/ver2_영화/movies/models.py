from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    summary = models.TextField()
    movie_image = models.ImageField(blank=True, upload_to='%Y%m%d/')