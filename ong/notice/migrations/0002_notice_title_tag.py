# Generated by Django 4.1 on 2022-08-17 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='title_tag',
            field=models.CharField(default='Noticia Nueva', max_length=255),
        ),
    ]
