# Generated by Django 4.0.6 on 2022-07-28 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='static/avatars/default.jpg', null=True, upload_to='static/avatars/'),
        ),
    ]