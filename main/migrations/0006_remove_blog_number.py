# Generated by Django 4.0.4 on 2023-01-10 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_blog_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='number',
        ),
    ]