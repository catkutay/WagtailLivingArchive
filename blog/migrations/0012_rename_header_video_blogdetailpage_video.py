# Generated by Django 3.2.12 on 2022-07-10 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20220710_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogdetailpage',
            old_name='header_video',
            new_name='video',
        ),
    ]
