# Generated by Django 3.0.8 on 2020-07-29 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_auto_20200729_1456'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={},
        ),
        migrations.RemoveField(
            model_name='photo',
            name='name',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='p_id',
        ),
    ]
