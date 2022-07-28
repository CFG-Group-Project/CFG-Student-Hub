# Generated by Django 4.0.6 on 2022-07-28 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_remove_profile_number_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='userprofile/static/avatars/'),
        ),
    ]
