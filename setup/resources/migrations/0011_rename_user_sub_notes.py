# Generated by Django 4.0.6 on 2022-07-29 11:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resources', '0010_alter_user_sub_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_sub',
            new_name='Notes',
        ),
    ]
