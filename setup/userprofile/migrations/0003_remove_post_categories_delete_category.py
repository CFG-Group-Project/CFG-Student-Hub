# Generated by Django 4.0.6 on 2022-08-09 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_alter_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
