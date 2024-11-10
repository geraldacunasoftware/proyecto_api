from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    
