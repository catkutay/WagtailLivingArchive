# Generated by Django 3.2.12 on 2022-11-12 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('blog', '0018_modules'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Modules',
        ),
    ]
