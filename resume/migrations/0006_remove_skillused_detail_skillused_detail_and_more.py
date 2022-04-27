# Generated by Django 4.0.4 on 2022-04-27 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_project_technology_skillused'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skillused',
            name='detail',
        ),
        migrations.AddField(
            model_name='skillused',
            name='detail',
            field=models.ManyToManyField(to='resume.detail'),
        ),
        migrations.RemoveField(
            model_name='technology',
            name='project',
        ),
        migrations.AddField(
            model_name='technology',
            name='project',
            field=models.ManyToManyField(to='resume.project'),
        ),
    ]