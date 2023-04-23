from django.db import models
from django.contrib.auth.models import User


class costsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=150)
    explanation = models.CharField(max_length=500)
    price = models.PositiveIntegerField()
    time = models.DateTimeField()
