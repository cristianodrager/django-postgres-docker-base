from django.db import models
from family.models import LegalRep

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100) 
    legal_rep = models.ManyToManyField(LegalRep, related_name='student')

    def __str__(self):
        return self.name