# Generated by Django 4.2.1 on 2023-05-12 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=255, verbose_name='ФИО'),
        ),
    ]
