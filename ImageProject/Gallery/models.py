from django.db import models

# Create your models here.
class ImageData(models.Model):
    category = models.CharField(max_length=20)
    Img = models.ImageField(upload_to='MyFavourite')
    date =models.DateField(auto_now_add=True)