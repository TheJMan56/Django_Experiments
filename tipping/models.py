from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    publisher = models.CharField(max_length=80)
    description = models.TextField()
