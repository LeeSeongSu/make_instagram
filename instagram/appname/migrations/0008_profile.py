# Generated by Django 3.0.8 on 2020-08-03 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0007_auto_20200803_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('nickname', models.CharField(blank=True, max_length=40)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
