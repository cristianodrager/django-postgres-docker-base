from django.db import models
from family.models import LegalRep


# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    # legal_rep = models.ManyToManyField(LegalRep, related_name="student")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Estudante"
        verbose_name_plural = "Estudantes"


class LegalRepStudent(models.Model):
    CHOICES = [
        ("Pai", "Pai"),
        ("Mãe", "Mãe"),
        ("Avô", "Avô"),
        ("Avó", "Avó"),
        ("Tio", "Tio"),
        ("Tia", "Tia"),
        ("Irmão", "Irmão"),
        ("Irmã", "Irmã"),
        ("Amigo da família", "Amigo da família"),
        ("Parente de 3º grau", "Parente de 3º grau"),
        ("Responsável legal", "Responsável legal"),
        ("Outro", "Outro"),
    ]
    legal_rep = models.ForeignKey(
        LegalRep, on_delete=models.CASCADE, related_name="legalrepstudent"
    )
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="legalrepstudent"
    )
    legal_rep_type = models.CharField(max_length=100, choices=CHOICES)

    def __str__(self):
        return f"{self.legal_rep.name} - {self.student.name}"

    class Meta:
        verbose_name = "Responsável Legal do Estudante"
        verbose_name_plural = "Responsáveis Legais dos Estudantes"
