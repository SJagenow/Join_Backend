from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=40)
    email =  models.CharField(max_length=40)
    phone = models.DecimalField(max_digits=20, decimal_places=0)

    def __str__(self):
        return self.name
    

class Tasks(models.Model):
    title = models.CharField(max_length=50) 
    description = models.TextField()
    Assignet_to = models.CharField(max_length=50)
    due_date = models.DecimalField(max_digits=50,decimal_places=4)
    prio     = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    subtasks = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.title}"