from django.shortcuts import render, HttpResponseRedirect 
from accounts.forms import AccountUserLoginForm
from accounts.forms import AccountUserRegisterForm
from accounts.forms import AccountUserEditForm
from django.contrib import auth
from django.urls import reverse 

def login(request):
    title = 'вход'
    
    login_form = AccountUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:            
            auth.login(request, user)       
            return HttpResponseRedirect(reverse('main')) 
        
        
    content = {'title' : title, 'login_form': login_form}
    return render(request, 'accounts/login.html', content)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main')) 

def register(request):
    title = 'Регистрация'
    
    if request.method == 'POST':
        register_form = AccountUserRegisterForm(request.POST, request.FILES)
        
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = AccountUserRegisterForm()
        
    content = {'title': title, 'register_form': register_form} 
        
    return render(request, 'accounts/register.html', content)
    
def edit(request):
    title = 'Редактирование'
    
    if request.method == 'POST':
        edit_form = AccountUserEditForm(request.POST, request.FILES, instance=request.user) 
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = AccountUserEditForm(instance=request.user)
            
    content = {'title': title, 'edit_form': edit_form}
    
    return render(request, 'accounts/edit.html', content) 