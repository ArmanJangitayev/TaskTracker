# Generated by Django 4.2.9 on 2024-02-04 01:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Task', '0002_alter_task_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dead_line',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
