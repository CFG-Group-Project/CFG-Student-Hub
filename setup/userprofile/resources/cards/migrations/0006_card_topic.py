# Generated by Django 4.0.6 on 2022-08-10 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_remove_card_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='topic',
            field=models.ManyToManyField(to='cards.topics'),
        ),
    ]
