# Generated by Django 4.2.5 on 2023-10-29 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_cartdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]