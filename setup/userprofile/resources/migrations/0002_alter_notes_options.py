# Generated by Django 4.0.6 on 2022-08-04 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name': 'Student note', 'verbose_name_plural': 'Student notes'},
        ),
    ]
