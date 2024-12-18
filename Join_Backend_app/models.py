

from django.db import models


# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=40)
    mail = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name if self.name else 'No name'

    

class Tasks(models.Model):
    PRIORITY_CHOICES = [
        ('urgent', 'Urgent'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    CATEGORY_CHOICES = [
        ('todos', 'Todos'), 
        ('inprogress', 'In Progress'),
        ('await', 'Awaiting Feedback'),
        ('done', 'Done'),
    ]
    LABEL_CHOICES = [
        ('CSS', 'CSS'), 
        ('JS', 'JS'),
        ('Testing', 'Testing'),
        ('User Story', 'User Story'),
        ('Technical Task', 'Technical Task'),
        ('HTML', 'HTML'),
    ]
    title = models.CharField(max_length=50)
    description = models.TextField()
    contacts = models.ManyToManyField(Profile, related_name='tasks')
    dueDate = models.DateField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default= 'Urgent')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='todos')
    label = models.CharField(max_length=20, choices=LABEL_CHOICES, default='CSS')

    def __str__(self):
        return self.title
     
class Subtask(models.Model):
    title = models.CharField(max_length=100, default='No Title')
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name='subtasks')
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} (Task: {self.task.title})"

    def is_done(self):
        return self.done
    
