# Generated by Django 3.1.1 on 2020-12-15 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Author',
            new_name='author',
        ),
    ]
