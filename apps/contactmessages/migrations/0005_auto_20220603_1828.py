# Generated by Django 2.2.1 on 2022-06-03 23:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contactmessages', '0004_auto_20220603_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessageinfo',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='add_time'),
        ),
    ]