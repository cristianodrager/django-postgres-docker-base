from django.shortcuts import render
from django.http import JsonResponse
import json
import numpy as np

from family.models import LegalRep


def face_login(request):

    return render(request, "face_login.html")


def face_scanner(request):
    cpf_hash = request.GET.get("cpf_hash", None)
    return render(request, "face_scanner.html", {"cpf_hash": cpf_hash})


def register_face(request):
    if request.method == "POST":

        data = json.loads(request.body)
        cpf_hash = data.get("cpf_hash")
        descriptor = data.get("descriptor")
        print(f"Descriptor data: {descriptor}")

        LegalRep.objects.filter(cpf_hash=cpf_hash).update(descriptor=descriptor)

        legal_rep = LegalRep.objects.filter(cpf_hash=cpf_hash).first()

        return JsonResponse(
            {
                "success": 1,
                "name": legal_rep.name,
                "cpf_hash": legal_rep.cpf_hash,
                "descriptor": legal_rep.descriptor,
            }
        )


def face_recognition(request):
    if request.method == "POST":

        data = json.loads(request.body)
        descriptor = data.get("descriptor")
        legal_reps = LegalRep.objects.all()
        input_descriptor = np.array(descriptor, dtype=np.float32)

        for face in legal_reps:
            stored_descriptor = np.array(face.descriptor, dtype=np.float32)
            distance = np.linalg.norm(input_descriptor - stored_descriptor)

            if distance < 0.6:
                return JsonResponse({"success": 1, "cpf_hash": face.cpf_hash})

    return JsonResponse({"success": 0})
