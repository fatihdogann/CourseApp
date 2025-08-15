from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Hoş geldiniz, {username}!")
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username} için hesap oluşturuldu. Şimdi giriş yapabilirsiniz.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, "Başarıyla çıkış yaptınız.")
    return redirect('index')