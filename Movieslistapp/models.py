from django.db import models


# Create your models here.
class MoviesInfo(models.Model):
    movies_name = models.CharField(max_length=200)
    movies_date = models.DateField(verbose_name="Date of a delivery")
