# Generated by Django 3.2.3 on 2021-06-22 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_comments_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='picture',
        ),
    ]
