from django.db import models
from django.db.models.fields.files import ImageField
from PIL import Image
import os


class Item(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Photo(models.Model):
    item = models.ForeignKey(Item)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=250)

    def __str__(self):
        return self.title
