# Generated by Django 5.1.3 on 2024-11-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Join_Backend_app', '0010_alter_tasks_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='category',
            field=models.CharField(choices=[('todos', 'Todos'), ('inprogress', 'In Progress'), ('await', 'Awaiting Feedback'), ('done', 'Done')], default='todo', max_length=20),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='label',
            field=models.CharField(choices=[('CSS', 'css'), ('JS', 'js'), ('Testing', 'testing'), ('User Story', 'userstory'), ('Technical Task', 'technicaltask'), ('HTML', 'html')], default='CSS', max_length=20),
        ),
    ]
