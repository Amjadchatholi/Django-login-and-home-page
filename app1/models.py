from unittest.util import _MAX_LENGTH
from xml.parsers.expat import model
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=245)
    images = models.CharField(max_length=2500)
    description = models.TextField(max_length=255)

    def __str__(self):
            return self.name