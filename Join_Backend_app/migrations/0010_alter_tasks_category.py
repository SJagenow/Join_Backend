# Generated by Django 5.1.3 on 2024-11-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Join_Backend_app', '0009_remove_tasks_contacts_tasks_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='category',
            field=models.CharField(choices=[('todo', 'Todo'), ('inprogress', 'In Progress'), ('await', 'Awaiting Feedback'), ('done', 'Done')], default='todo', max_length=20),
        ),
    ]