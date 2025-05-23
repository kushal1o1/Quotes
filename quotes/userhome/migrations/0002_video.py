# Generated by Django 5.0.1 on 2024-01-11 12:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userhome', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('video_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
