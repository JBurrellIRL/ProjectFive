# Generated by Django 3.2 on 2022-11-23 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order_notes', models.TextField()),
                ('related_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_order', to='checkout.order')),
            ],
            options={
                'verbose_name_plural': 'Order Notes',
            },
        ),
    ]