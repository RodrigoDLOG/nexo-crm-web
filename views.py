from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, "core/login.html", {'form': AuthenticationForm()})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            return render(request, "core/login.html", {
                'form': AuthenticationForm(),
                'error': 'Usuario o contraseña incorrectos'
            })

        login(request, user)

        if user.is_staff:
            return redirect('/admin/')
        else:
            return redirect('polizas')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')
