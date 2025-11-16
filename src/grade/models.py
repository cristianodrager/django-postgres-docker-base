from django.db import models
from django.contrib.auth.models import User
from student.models import Student
from family.models import LegalRep

# Create your models here.
class Turma(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    users = models.ManyToManyField(User, related_name='turmas')
    students = models.ManyToManyField(Student, related_name='turmas')
    #school = models.ForeignKey('school.School', on_delete=models.CASCADE, related_name='turmas')

    def __str__(self):
        return self.name
    
class Disciplina(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Presenca(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, null=True, blank=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"

class RegistroSaida(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    picked_up_by = models.ForeignKey(LegalRep, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.time} - {self.picked_up_by}"
    
class ConfirmacaoSaida(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.time}"