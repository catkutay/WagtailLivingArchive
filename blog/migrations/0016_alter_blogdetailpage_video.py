# Generated by Django 3.2.12 on 2022-07-31 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailvideos', '0012_remove_unique_constraint'),
        ('blog', '0015_alter_blogdetailpage_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailvideos.video'),
        ),
    ]
