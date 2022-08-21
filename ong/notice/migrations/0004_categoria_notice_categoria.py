# Generated by Django 4.1 on 2022-08-19 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0003_notice_fecha_publicacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='notice',
            name='categoria',
            field=models.CharField(default='Noticias', max_length=250),
        ),
    ]
