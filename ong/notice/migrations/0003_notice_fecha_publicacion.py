# Generated by Django 4.1 on 2022-08-18 01:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_notice_title_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='fecha_publicacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]