# Generated by Django 3.2.3 on 2021-06-22 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_rename_thead_comments_thread'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='picture',
            field=models.FileField(null=True, upload_to='media/'),
        ),
    ]
