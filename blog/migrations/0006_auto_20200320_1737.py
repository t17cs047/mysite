# Generated by Django 2.2.1 on 2020-03-20 08:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200320_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_time',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
