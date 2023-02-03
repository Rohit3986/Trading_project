from django.db import models
import os
# Create your models here.

class CsvFiles(models.Model):
    file = models.FileField(upload_to="file_uploads")

class Candles(models.Model):
    Date = models.CharField(max_length=30)
    Open = models.CharField(max_length=30)
    High = models.CharField(max_length=30)
    Low = models.CharField(max_length=30)
    Close = models.CharField(max_length=30)

