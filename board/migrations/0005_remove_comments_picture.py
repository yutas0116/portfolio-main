# Generated by Django 3.2.3 on 2021-06-22 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_alter_comments_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='picture',
        ),
    ]