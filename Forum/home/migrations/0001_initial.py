# Generated by Django 2.0.1 on 2018-04-30 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('photo', models.FileField(blank=True, upload_to='posts')),
                ('content', models.TextField()),
                ('dept', models.CharField(choices=[('ALL', 'ALL'), ('CSE', 'CSE'), ('ECE', 'ECE'), ('IT', 'IT'), ('EE', 'EE'), ('AEIE', 'AEIE')], default='ALL', max_length=5)),
                ('year', models.CharField(choices=[('ALL', 'ALL'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017')], default='ALL', max_length=4)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('time_now', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
