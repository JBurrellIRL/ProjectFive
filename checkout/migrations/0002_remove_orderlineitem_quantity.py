# Generated by Django 3.2 on 2022-11-13 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='quantity',
        ),
    ]