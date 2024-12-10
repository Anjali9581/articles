from django.db import models

# Create your models here.
class Articles(models.Model):
    name = models.CharField(max_length=52)
    description = models.CharField(max_length=1100)
    def __str__(self):
        return self.name