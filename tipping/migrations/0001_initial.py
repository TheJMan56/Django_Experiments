# Generated by Django 3.2.18 on 2023-05-03 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('author', models.CharField(max_length=80)),
                ('publisher', models.CharField(max_length=80)),
                ('description', models.TextField()),
            ],
        ),
    ]
