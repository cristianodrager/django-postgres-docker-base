from django.db import models

# Create your models here.
class Turma(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    #users = models.ManyToManyField('auth.User', related_name='turmas')
    #students = models.ManyToManyField('student.Student', related_name='turmas')
    #school = models.ForeignKey('school.School', on_delete=models.CASCADE, related_name='turmas')

    def __str__(self):
        return self.name
    
class Disciplina(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Presenca(models.Model):
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)  # e.g., 'Present', 'Absent'

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"

class RegistroSaida(models.Model):
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    picked_up_by = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.time} - {self.picked_up_by}"
    
class ConfirmacaoSaida(models.Model):
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    date = models.DateField()
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {'Confirmed' if self.confirmed else 'Not Confirmed'}"