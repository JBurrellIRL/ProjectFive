# Generated by Django 3.2 on 2022-11-19 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_remove_reviews_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]
