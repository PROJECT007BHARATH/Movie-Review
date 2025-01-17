# Generated by Django 4.2.10 on 2024-05-03 11:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0008_alter_movie_trailer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='anonymous', max_length=50)),
                ('review_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('stars', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('comment', models.TextField(max_length=5000)),
                ('Movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.movie')),
            ],
        ),
    ]
