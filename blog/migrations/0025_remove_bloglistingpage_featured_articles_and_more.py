# Generated by Django 4.1.8 on 2023-05-06 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_bloglistingpage_featured_articles_featuredarticle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloglistingpage',
            name='featured_articles',
        ),
        migrations.DeleteModel(
            name='FeaturedArticle',
        ),
    ]
