# Generated by Django 3.2 on 2022-11-19 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20221119_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='name',
        ),
    ]
