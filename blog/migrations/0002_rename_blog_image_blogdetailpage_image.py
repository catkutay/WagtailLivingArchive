# Generated by Django 3.2.12 on 2022-03-27 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogdetailpage',
            old_name='blog_image',
            new_name='image',
        ),
    ]
