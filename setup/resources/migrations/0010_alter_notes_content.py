# Generated by Django 4.0.6 on 2022-08-09 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0009_alter_material_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='content',
            field=models.TextField(max_length=10000),
        ),
    ]
