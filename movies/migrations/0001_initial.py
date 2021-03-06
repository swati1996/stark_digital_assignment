# Generated by Django 3.1.3 on 2020-11-11 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=250)),
                ('popularity', models.FloatField()),
                ('director', models.CharField(default=None, max_length=220)),
                ('imdb_score', models.FloatField()),
                ('genre', models.ManyToManyField(to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster_url', models.CharField(default=None, max_length=250)),
                ('movie_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_name', to='movies.movie')),
            ],
        ),
    ]
