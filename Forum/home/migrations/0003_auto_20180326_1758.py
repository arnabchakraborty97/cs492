# Generated by Django 2.0.3 on 2018-03-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180324_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.FileField(blank=True, upload_to='posts'),
        ),
    ]