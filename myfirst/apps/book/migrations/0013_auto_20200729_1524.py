# Generated by Django 3.0.8 on 2020-07-29 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_auto_20200729_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Фамилия пользователя')),
                ('second_name', models.CharField(max_length=20, verbose_name='Имя пользователя')),
            ],
        ),
        migrations.DeleteModel(
            name='oga',
        ),
    ]