# Generated by Django 5.1.3 on 2024-11-20 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Join_Backend_app', '0002_tasks_label'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtask',
            old_name='status',
            new_name='done',
        ),
    ]