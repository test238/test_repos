# Generated by Django 3.0.5 on 2020-05-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_api1_forecast', '0002_city2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city2',
            name='name',
            field=models.CharField(default='test1', max_length=25),
        ),
        migrations.AlterField(
            model_name='city2',
            name='name2',
            field=models.CharField(default='test2', max_length=25),
        ),
    ]