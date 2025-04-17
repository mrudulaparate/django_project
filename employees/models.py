from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField()

    def __str__(self):
        return self.name
