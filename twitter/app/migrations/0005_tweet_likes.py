# Generated by Django 2.1.7 on 2019-03-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190302_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
