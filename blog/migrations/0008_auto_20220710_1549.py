# Generated by Django 3.2.12 on 2022-07-10 06:19

from django.db import migrations
import mirage.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blogdetailpage_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='body',
            field=mirage.fields.EncryptedTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='blogdetailpage',
            name='intro',
            field=mirage.fields.EncryptedCharField(max_length=250),
        ),
    ]
