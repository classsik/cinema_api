# Generated by Django 4.1.7 on 2023-03-09 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=150)),
                ('year_of_birth', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publish_year', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.director')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('films', models.ManyToManyField(to='main.film')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.genre'),
        ),
    ]
