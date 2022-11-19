# Generated by Django 3.2 on 2022-11-19 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20221119_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, '1 - Awful'), (2, '2 - Poor'), (3, '3 - Average'), (4, '4 - Good'), (5, '5 - Excellent')], null=True),
        ),
    ]
