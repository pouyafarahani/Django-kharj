# Generated by Django 4.2 on 2023-04-23 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costsmodel',
            name='name',
            field=models.CharField(max_length=150, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='costsmodel',
            name='time',
            field=models.DateField(),
        ),
    ]
