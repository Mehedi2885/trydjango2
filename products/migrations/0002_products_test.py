# Generated by Django 3.0.5 on 2020-04-17 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='test',
            field=models.TextField(default='Testing'),
            preserve_default=False,
        ),
    ]
