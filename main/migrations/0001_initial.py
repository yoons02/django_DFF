# Generated by Django 4.0.4 on 2023-01-15 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=20)),
                ('writer', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField()),
            ],
        ),
    ]
