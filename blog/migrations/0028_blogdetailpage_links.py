# Generated by Django 4.1.8 on 2023-05-06 11:27

from django.db import migrations
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_remove_blogdetailpage_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdetailpage',
            name='links',
            field=wagtail.fields.StreamField([('link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Enter the link title', required=True)), ('url', wagtail.blocks.CharBlock(help_text='Enter the link URL', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='Choose a document for this link', required=False))]))], blank=True, use_json_field=True),
        ),
    ]
