# Generated by Django 3.1.1 on 2020-12-13 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='thumbnail',
            new_name='thumb',
        ),
    ]
