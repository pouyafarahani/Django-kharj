from django.db import models
from django.contrib.auth.models import User


class costsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=150, verbose_name='تیتر')
    explanation = models.CharField(max_length=500, verbose_name='توضیح')
    price = models.PositiveIntegerField(verbose_name='قیمت')
    time = models.CharField(max_length=50, verbose_name='تاریخ')

    def __str__(self):
        return f'{self.user}: {self.name}: {self.price}'
