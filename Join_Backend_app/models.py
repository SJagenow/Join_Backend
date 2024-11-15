from django.db import models


# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=40)
    mail =  models.CharField(max_length=40)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Tasks(models.Model):
    title = models.CharField(max_length=50) 
    description = models.TextField()
    contacts = models.CharField(max_length=50)
    dueDate = models.DecimalField(max_digits=50,decimal_places=4)
    priority   = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    subtasks = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.title}"