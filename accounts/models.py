from django.db import models


class RegisterModel(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

