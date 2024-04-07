# Generated by Django 3.0.7 on 2024-04-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20240404_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_1',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_3',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_4',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]