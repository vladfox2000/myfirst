# Generated by Django 3.0.8 on 2020-07-29 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Фото пользователя '},
        ),
        migrations.AlterField(
            model_name='photo',
            name='img',
            field=models.ImageField(height_field=100, upload_to='', width_field=100),
        ),
    ]
