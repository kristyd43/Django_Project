# Generated by Django 3.2.5 on 2021-08-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='ing',
            field=models.URLField(default='https://placedog.net/800/640?id=5'),
        ),
    ]
