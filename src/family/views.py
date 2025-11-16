from django.shortcuts import render, HttpResponse
from .models import LegalRep
from student.models import Student

# Create your views here.
def family(request, cpf):
    legal_rep = LegalRep.objects.filter(cpf=cpf).first()
    students = Student.objects.filter(legal_rep=legal_rep)
    if legal_rep:
        return render(request, 'family.html', {'legal_rep': legal_rep, 'students': students})
    return HttpResponse(f"Sem resultados para o CPF: {cpf}")