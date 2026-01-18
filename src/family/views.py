from django.shortcuts import render, HttpResponse, redirect
from .models import LegalRep
from student.models import Student, LegalRepStudent
from student.models import Student
from grade.models import Turma, Presenca, RegistroSaida, ConfirmacaoSaida
import datetime


def family(request, cpf):
    # legal_rep = LegalRep.objects.filter(cpf__icontains=cpf[:4]).first()
    hashed = hash_cpf(cpf.strip())
    legal_rep = LegalRep.objects.filter(cpf_hash=hash_cpf(cpf)).first()

    if legal_rep:
        query_students = LegalRepStudent.objects.filter(legal_rep=legal_rep).all()
        # turma = Turma.objects.get(pk=id)
        students = []
        for ls in query_students:
            students.append(
                Student.objects.filter(id=ls.student.id).first()
            )  # Acessa o estudante relacionado para evitar consultas adicionais
        # verificar se estudante está presente no dia
        # verificar se estudante já saiu e quem buscou
        for student in students:
            student.presenca = Presenca.objects.filter(
                date=datetime.date.today(), student=student
            )
            student.registro_saida = RegistroSaida.objects.filter(
                date=datetime.date.today(), student=student
            )
            student.confirmacao_saida = ConfirmacaoSaida.objects.filter(
                date=datetime.date.today(), student=student
            )
        return render(
            request, "family.html", {"legal_rep": legal_rep, "students": students}
        )
    return HttpResponse(f"Sem resultados para o CPF: {cpf} e hash: {hashed} ")


def family_face(request):
    cpf_hash = request.GET.get("cpf_hash", None)
    legal_rep = LegalRep.objects.filter(cpf_hash=cpf_hash).first()

    if legal_rep:
        query_students = LegalRepStudent.objects.filter(legal_rep=legal_rep).all()
        # turma = Turma.objects.get(pk=id)
        students = []
        for ls in query_students:
            students.append(
                Student.objects.filter(id=ls.student.id).first()
            )  # Acessa o estudante relacionado para evitar consultas adicionais
        # verificar se estudante está presente no dia
        # verificar se estudante já saiu e quem buscou
        for student in students:
            student.presenca = Presenca.objects.filter(
                date=datetime.date.today(), student=student
            )
            student.registro_saida = RegistroSaida.objects.filter(
                date=datetime.date.today(), student=student
            )
            student.confirmacao_saida = ConfirmacaoSaida.objects.filter(
                date=datetime.date.today(), student=student
            )
        return render(
            request, "family.html", {"legal_rep": legal_rep, "students": students}
        )
    return HttpResponse(f"Erro ao localizar família.")


def search_family(request, pk):
    cpf = request.GET.get("cpf")
    if cpf:
        legal_reps = LegalRep.objects.filter(cpf__icontains=cpf).all()
        relationships = LegalRepStudent.CHOICES
        return render(
            request,
            "search_family.html",
            {
                "legal_reps": legal_reps,
                "student_id": pk,
                "relationships": relationships,
            },
        )
    return HttpResponse("Nenhum CPF fornecido.")


def add_family_save(request):
    if request.method == "POST":
        student = request.POST.get("student")
        name = request.POST.get("name")
        email = request.POST.get("email")
        cpf = request.POST.get("cpf")
        phone = request.POST.get("phone")
        hashed_cpf = hash_cpf(cpf)
        # verificar se já existe
        if request.POST.get("cpf_hash"):
            hashed_cpf = request.POST.get("cpf_hash")
            existing_legal = LegalRep.objects.filter(cpf_hash=hashed_cpf).first()

            if existing_legal:
                # editar dados
                existing_legal.name = name
                existing_legal.email = email
                existing_legal.phone = phone
                existing_legal.save()
                if student != None:
                    return redirect("student", id=student)
                return redirect("add-family")

        legal_rep = LegalRep(name=name, email=email, cpf=cpf, phone=phone)
        legal_rep.save()

        if student != None:
            return redirect("student", id=student)
    return redirect("add-family")


def add_family_form(request):
    student = request.GET.get("student_id", None)
    return render(request, "add_family.html", {"student": student})


def edit_family_form(request):
    cpf_hash = request.GET.get("cpf_hash", None)
    student = request.GET.get("student_id", None)
    legal_resp = LegalRep.objects.filter(cpf_hash=cpf_hash).first()
    return render(
        request, "edit_family.html", {"legal_resp": legal_resp, "student": student}
    )


def hash_cpf(cpf):
    import os
    import hashlib
    import hmac

    secret_key = os.environ.get("SECRET_KEY", "default_secret_key")
    cpf_hash = hmac.new(
        key=secret_key.encode(),
        msg=cpf.encode(),
        digestmod=hashlib.sha256,
    ).hexdigest()

    return cpf_hash
