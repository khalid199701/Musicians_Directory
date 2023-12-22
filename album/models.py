from django.db import models
from musician.models import Musician
# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length = 200)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateTimeField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.album_name