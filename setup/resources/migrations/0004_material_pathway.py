# Generated by Django 4.0.6 on 2022-08-02 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='pathway',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='resources.program'),
        ),
    ]
