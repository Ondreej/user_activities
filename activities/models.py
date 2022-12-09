from django.db import models

class Activity(models.Model):
    description = models.CharField(max_length=200)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
