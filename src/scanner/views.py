from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def scanner(request):
    return render(request, 'scanner.html')

def scanner_read(request, cpf): #recebe o CPF lido e redireciona para a view family que mostra os alunos associados ao cpf
    return redirect('family', cpf=cpf)