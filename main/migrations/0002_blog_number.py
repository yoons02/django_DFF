# Generated by Django 4.0.4 on 2023-01-10 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]
