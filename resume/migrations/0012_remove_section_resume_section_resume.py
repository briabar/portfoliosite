# Generated by Django 4.0.4 on 2022-04-29 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0011_alter_project_section_remove_section_resume_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='resume',
        ),
        migrations.AddField(
            model_name='section',
            name='resume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume'),
        ),
    ]
