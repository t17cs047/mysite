# Generated by Django 2.2.1 on 2020-03-20 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='thumnail/'),
        ),
    ]
