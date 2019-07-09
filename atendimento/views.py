from django.shortcuts import render
from . models import Cliente
# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/list.html', {'clientes':clientes})
def cliente_delete (request, cliente_id):
    cliente = Cliente.objects.get(pk= cliente_id)
    cliente.delete()
    return redirect('/atendimento/cliente/')