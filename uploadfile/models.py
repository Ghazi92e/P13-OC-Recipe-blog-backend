from django.db import models

# Create your models here.

class Uploadfile(models.Model):
    file = models.FileField(blank=False, null=False)