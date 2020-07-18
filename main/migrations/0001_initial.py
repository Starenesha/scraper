# Generated by Django 3.0.8 on 2020-07-17 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='title')),
                ('url', models.CharField(max_length=200, verbose_name='url')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date')),
                ('value', models.CharField(max_length=20, verbose_name='value')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Series')),
            ],
        ),
    ]