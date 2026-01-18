from django.shortcuts import render, HttpResponse
from grade.models import RegistroSaida, Turma
import datetime


# Create your views here.
def monitor_sala(request):
    get_turmas = request.GET.getlist("turma")
    get_turmas = [int(turma) for turma in get_turmas if turma.isdigit()]
    alunos = RegistroSaida.objects.filter(
        turma__id__in=get_turmas, date=datetime.date.today()
    ).all()

    turmas = Turma.objects.filter(year=datetime.date.today().year).all()

    return render(
        request,
        "monitor_sala.html",
        {"alunos": alunos, "turmas": turmas, "get_turmas": get_turmas},
    )
