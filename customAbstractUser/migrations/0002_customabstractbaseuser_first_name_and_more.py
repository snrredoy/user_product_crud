# Generated by Django 5.1.4 on 2025-01-02 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customAbstractUser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customabstractbaseuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='First Name '),
        ),
        migrations.AddField(
            model_name='customabstractbaseuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Last Name '),
        ),
    ]