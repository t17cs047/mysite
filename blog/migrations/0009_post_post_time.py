# Generated by Django 2.2.1 on 2020-03-20 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_post_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_time',
            field=models.DateField(null=True),
        ),
    ]