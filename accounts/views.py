from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'POST':
        username =  request.POST.get('username')
        password =  request.POST.get('password')

        userVerify = auth.authenticate(request, username=username, password=password)
        print(userVerify)
        if userVerify == None:
            messages.info(request, "usuário ou senha invalido(s)")
            return redirect('login')
        else:
            auth.login(request,userVerify)
            return redirect('home')
    
    else:
        return render(request, 'pages/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('rPassword')

        # Verifica se o nome de usuário contém apenas espaços em branco ou está vazio
        if username.isspace() or not username:
            messages.error(request, 'Nome de usuário inválido. Por favor, insira um nome de usuário válido.')
            return redirect('register')

        # Restante do seu código de validação aqui...

        # Cria o usuário apenas se a validação passar
        User.objects.create_user(username=username, email=email, password=password)

        return redirect('login')

    else:
        return render(request, 'pages/register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
