# Generated by Django 2.0.5 on 2019-08-15 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0006_auto_20190807_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
    ]
