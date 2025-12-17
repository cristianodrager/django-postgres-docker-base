from django.shortcuts import render, redirect, HttpResponse
from .models import Turma, Disciplina, Presenca, RegistroSaida, ConfirmacaoSaida
from student.models import Student
import datetime


# Create your views here.
def turmas(request):
    turmas = Turma.objects.all()
    anos = Turma.objects.values_list("year", flat=True).distinct().order_by("-year")
    return render(request, "turmas.html", {"turmas": turmas, "anos": anos})


def turma(request, id):
    turma = Turma.objects.get(pk=id)
    students = turma.students.all()
    for student in students:
        student.presenca = Presenca.objects.filter(
            turma=turma, date=datetime.date.today(), student=student
        )

    # presença no dia?
    return render(request, "turma.html", {"turma": turma, "students": students})


def turmas_filter(request):
    filter = request.GET.get("search-turma", "")
    filter_spliter = filter.split(" ")
    ano = request.GET.get("ano", "")

    turmas = Turma.objects.filter(
        name__icontains=filter_spliter[0], year__icontains=ano
    )

    for term in filter_spliter[1:]:
        turmas = turmas.filter(name__icontains=term, year__icontains=ano)

    return render(request, "turmas-filter.html", {"turmas": turmas})


def turmas_filter_search(request, student_id):
    filter = request.GET.get("search-turma", "")
    filter_spliter = filter.split()
    ano = request.GET.get("ano", "")

    turmas = Turma.objects.filter(
        name__icontains=filter_spliter[0], year__icontains=ano
    )

    for term in filter_spliter[1:]:
        turmas = turmas.filter(name__icontains=term, year__icontains=ano)

    return render(
        request,
        "turmas-filter-search.html",
        {"turmas": turmas, "student_id": student_id},
    )


def add_student_turma(request, turma_id, student_id):
    turma = Turma.objects.filter(pk=turma_id).first()
    student = Student.objects.filter(pk=student_id).first()

    if turma and student:
        turma.students.add(student)
        turma.save()

    return redirect("student", id=student_id)


def remove_student_turma(request, turma_id, student_id):
    if request.method == "DELETE":
        turma = Turma.objects.filter(pk=turma_id).first()
        student = Student.objects.filter(pk=student_id).first()

        if turma and student:
            turma.students.remove(student)
            turma.save()
            return HttpResponse("Atividade removida com sucesso", status=200)

    return HttpResponse("Método não permitido", status=405)
