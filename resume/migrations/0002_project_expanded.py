# Generated by Django 4.0.4 on 2022-05-19 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='expanded',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
