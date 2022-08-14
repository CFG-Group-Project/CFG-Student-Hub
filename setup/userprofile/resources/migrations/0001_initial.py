# Generated by Django 4.0.6 on 2022-08-04 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('pathway', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=1000)),
                ('link', models.URLField(blank=True, max_length=250)),
                ('user', models.ForeignKey(default='CFG Grad', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Student Submission',
                'verbose_name_plural': 'Student Submissions',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.CharField(max_length=50, null=True)),
                ('week', models.CharField(max_length=3)),
                ('slides', models.CharField(max_length=400)),
                ('code_file', models.CharField(blank=True, max_length=400, null=True)),
                ('show', models.BooleanField(null=True)),
                ('topics', models.CharField(max_length=50, null=True)),
                ('rectutorial', models.URLField(unique=True)),
                ('pathway', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='resources.program')),
                ('sub_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
