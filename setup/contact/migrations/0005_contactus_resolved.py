# Generated by Django 4.0.6 on 2022-08-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_contactus_options_contactus_subbed'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
    ]