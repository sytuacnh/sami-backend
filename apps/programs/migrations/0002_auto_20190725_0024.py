# Generated by Django 2.2.1 on 2019-07-25 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programinfo',
            name='name',
        ),
        migrations.AddField(
            model_name='programinfo',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='program_title'),
        ),
    ]
