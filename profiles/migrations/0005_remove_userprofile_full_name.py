# Generated by Django 3.2 on 2022-11-15 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_userprofile_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='full_name',
        ),
    ]