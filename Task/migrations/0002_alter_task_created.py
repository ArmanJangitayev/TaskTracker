# Generated by Django 4.2.9 on 2024-02-04 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
