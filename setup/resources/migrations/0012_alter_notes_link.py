# Generated by Django 4.0.6 on 2022-07-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0011_rename_user_sub_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='link',
            field=models.URLField(blank=True, max_length=250),
        ),
    ]