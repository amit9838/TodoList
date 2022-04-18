from django.db import models

# Create your models here.

class Task(models.Model):
    taskName = models.CharField( max_length=50)
    taskDesc = models.TextField()
    time = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.taskName

    class Meta:
        ordering = ['-time']
