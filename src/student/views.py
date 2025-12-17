from django.shortcuts import render, redirect, HttpResponse
from .models import Student, LegalRepStudent
from family.models import LegalRep


def student(request, id):  # crud para responsáveis legais
    student = Student.objects.filter(id=id).first()
    turmas = student.turmas.all().order_by("name")
    legal = student.legalrepstudent.all().order_by("legal_rep__name")

    for lr in legal:
        print(f"Responsável: {lr.legal_rep.name} - Tipo: {lr.legal_rep_type}")

    return render(
        request,
        "student.html",
        {"student": student, "legals": legal, "turmas": turmas, "student_id": id},
    )


def search(request):  # htmx
    return render(request, "search_student.html")


def search_results(request):  # htmx
    query = request.GET.get("q", "")
    filter_spliter = query.split()
    # students = Student.objects.none()
    for term in filter_spliter:
        print(term)
        students = Student.objects.filter(name__icontains=term)

    return render(request, "search_student_results.html", {"students": students})


def add_legal_resp(request, student_id, legal_resp_id):
    student = Student.objects.filter(pk=student_id).first()
    legal_resp = LegalRep.objects.filter(pk=legal_resp_id).first()

    if student and legal_resp:
        # Adiciona o responsável legal ao estudante com um tipo padrão, por exemplo "Outro"
        # LegalRepStudent.objects.create(
        #     student=student, legal_resp=legal_resp, legal_resp_type="Outro"
        # )
        LegalRepStudent(
            student=student, legal_rep=legal_resp, legal_rep_type="Outro"
        ).save()

    # Redireciona de volta para a página do estudante
    return redirect("student", id=student_id)


def remove_legal_resp(request, legal_resp_student_id):
    if request.method == "DELETE":
        legal_resp_student = LegalRepStudent.objects.filter(
            pk=legal_resp_student_id
        ).first()
        legal_resp_student.delete()
        return HttpResponse("Responsável legal removido com sucesso.")

    return HttpResponse("Método não permitido.", status=405)
