from django.db import models

# Create your models here.


class Writer(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    name = models.CharField(max_length=100)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name='books')
