from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserAdminCreationForm, RegisterForm, LogInForm
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'index.html')


def login_view(request):
    context = {}
    form = LogInForm()
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':

        form = LogInForm(data=request.POST)

        if form.is_valid():
            # authenticate(username='email',password)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user:
                login(request, user)
                context['msg'] = "login successful"
                return redirect('/')
            else:
                context['msg'] = "invalid credentials"

    context['form'] = form
    return render(request, 'login.html', context)


def userlogin(request):
    context = {}
    form = LogInForm()
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':

        form = LogInForm(data=request.POST)

        if form.is_valid():
            # authenticate(username='email',password)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user:
                login(request, user)
                context['msg'] = "login successful"
                return redirect('/')
            else:
                context['msg'] = "invalid credentials"

    context['form'] = form
    return render(request, 'menu/userlogin.html', context)


def signup(request):
    context = {}
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, 'signup.html', context)


def usersignup(request):
    context = {}
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, 'menu/usersignup.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


def user_logout_view(request):
    logout(request)
    return redirect('userlogin')

#
# def signup(request):
#     context = {}
#     form = RegisterForm()
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         password_2 = request.POST.get('password_2')
#
#         form = RegisterForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             # return redirect('login')
#
#
#     # context['form'] = form
#
#     return render(request, 'signup.html', context={'form': form})

# def signup(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         password_2 = request.POST.get('password_2')
