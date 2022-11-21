from django.db import models

# Create your models here.
class Crutch(models.Model):
    name = models.CharField(max_length=255)
    datePublished = models.DateTimeField()
    description = models.TextField()
    price = models.IntegerField()
    imageField = models.ImageField(upload_to="uploads/")