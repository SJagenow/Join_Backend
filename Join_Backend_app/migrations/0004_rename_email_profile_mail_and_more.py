# Generated by Django 5.1.3 on 2024-11-15 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Join_Backend_app', '0003_alter_profile_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='email',
            new_name='mail',
        ),
        migrations.RenameField(
            model_name='tasks',
            old_name='Assignet_to',
            new_name='contacts',
        ),
        migrations.RenameField(
            model_name='tasks',
            old_name='due_date',
            new_name='dueDate',
        ),
        migrations.RenameField(
            model_name='tasks',
            old_name='prio',
            new_name='priority',
        ),
    ]
