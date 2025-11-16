from django.shortcuts import render
from .models import Turma, Disciplina, Presenca, RegistroSaida, ConfirmacaoSaida

# Create your views here.
def turmas(request):
    turmas = Turma.objects.all()
    return render(request, 'turmas.html', {'turmas':turmas})

def turma(request, id):
    turma = Turma.objects.get(pk=id)
    students = turma.students.all()
    return render(request, 'turma.html', {'turma': turma, 'students': students})