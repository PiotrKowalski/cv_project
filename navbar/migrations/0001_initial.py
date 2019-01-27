# Generated by Django 2.1.2 on 2018-10-27 12:22

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_API', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('url', models.SlugField(max_length=100, null=True)),
                ('type', models.CharField(choices=[('ANIME', 'ANIME'), ('MANGA', 'MANGA')], max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('status', models.CharField(choices=[('FINISHED', 'FINISHED'), ('RELEASING', 'RELEASING'), ('NOT_YET_RELEASED', 'NOT_YET_RELEASED'), ('CANCELLED', 'CANCELLED')], max_length=200, null=True)),
                ('season', models.CharField(choices=[('WINTER', 'WINTER'), ('SPRING', 'SPRING'), ('SUMMER', 'SUMMER'), ('FALL', 'FALL')], max_length=100, null=True)),
                ('episodes', models.IntegerField(null=True)),
                ('duration', models.IntegerField(null=True)),
                ('genres', models.CharField(max_length=500, null=True)),
                ('average_score', models.IntegerField(null=True)),
                ('trending', models.IntegerField(null=True)),
                ('popularity', models.IntegerField(null=True)),
                ('streaming_episodes', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500, null=True), null=True, size=2), null=True, size=None)),
                ('imageURL', models.CharField(max_length=500, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announcments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('Description', models.CharField(blank=True, max_length=2000)),
                ('text_on_searchbox', models.CharField(blank=True, max_length=2000)),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='NavTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('url', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]