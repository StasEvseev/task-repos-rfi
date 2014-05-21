from django.db import models

# Create your models here.

class Man(models.Model):
    name = models.CharField(max_length=32)
    follow_ids = models.TextField()