
from django.db import models


# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=40)
    mail =  models.CharField(max_length=40)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Tasks(models.Model):
     PRIORITY_CHOICES = [ ('low', 'Low'), ('medium', 'Medium'), ('urgent', 'Urgent'), ]
     title = models.CharField(max_length=50)
     description = models.TextField()
     contacts = models.CharField(max_length=50)
     dueDate = models.DateField()
     priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
     category = models.CharField(max_length=20)
   

     def __str__(self): 
      return self.title
     
class Subtask(models.Model):
    title = models.CharField(max_length=100)
   
    def __str__(self):
        return self.title

    
