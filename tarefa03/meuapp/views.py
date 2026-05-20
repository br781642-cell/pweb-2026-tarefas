from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def usuarios(request):

    lista_usuarios = [
        {
            'nome': 'Ana Clara',
            'matricula': '20241181110001',
            'idade': 18,
            'cidade': 'Natal'
        },
        {
            'nome': 'Bruno Rafael',
            'matricula': '20241181110002',
            'idade': 17,
            'cidade': 'São Paulo do Potengi'
        },
        {
            'nome': 'Carlos Henrique',
            'matricula': '20241181110003',
            'idade': 19,
            'cidade': 'Mossoró'
        },
        {
            'nome': 'Juliana Souza',
            'matricula': '20241181110004',
            'idade': 20,
            'cidade': 'Parnamirim'
        },
        {
            'nome': 'Marina Lima',
            'matricula': '20241181110005',
            'idade': 18,
            'cidade': 'Caicó'
        }
    ]

    context = {
        "usuarios": lista_usuarios
    }

    return render(request, 'usuarios.html', context)