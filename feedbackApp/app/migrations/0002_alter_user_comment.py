# Generated by Django 4.0.2 on 2022-02-12 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='comment',
            field=models.TextField(default='', max_length=5000),
        ),
    ]
