from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def user_list(request):
    users = User.objects.all()
    return render (request, 'user/list.html', {'users': users})

@permission_required("user_delete")
def user_delete (request, user_id):
    user = User.objects.get(pk = user_id)
    messages.success(request, "Operação concluida com sucesso.")
    user.delete()
    return redirect('/atendimento/atendimento/')
