# Generated by Django 3.0.5 on 2020-04-27 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelQuerySet', '0002_character_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Framework2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('language', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='modelQuerySet.Language2')),
            ],
        ),
    ]
