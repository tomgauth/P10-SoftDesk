from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=280)
    project_type = models.CharField(max_length=70)

    def __str__(self):
        return self.title
