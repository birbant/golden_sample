from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from samples.models import Samples
from employees.models import Employees
from management.models import SampleOperation


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('my-login')

    context = {'RegistrationForm': form}

    return render(request, 'acco/register.html', context)


def my_login(request, username=None):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are logged in as {username}.")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")

    context = {'LoginForm': form}

    return render(request, 'acco/my-login.html', context)


def user_logout(request):
    logout(request)
    messages.info(request, "You have been successfully logged out. Thank you for using Golden Sample application.")
    return render(request,'acco/user-logout.html')


@login_required
def dashboard(request):
    username = request.user.username

    support_contact = {
        'phone': '123-456-789',
        'email': 'kuba@golden-sample-app.com',
        'contact_form_url': '/contact/',  # Przykładowy URL do formularza kontaktowego
    }
    context = {'username': username,
               'support_contact': support_contact}

    return render(request, 'acco/dashboard.html', context)


def page_404(request):
    return render(request, '404.html', status=404)


def is_logged(request):
    context = {
        'is_logged': request.user.is_authenticated
    }
    return render(request, 'base.html', context)


def view_statistics(request):
    employees_count = Employees.objects.count()
    samples_count = Samples.objects.count()
    operations_count = SampleOperation.objects.count()
    context = {
        'employees_count': employees_count,
        'samples_count': samples_count,
        'operations_count': operations_count,
    }

    return render(request, 'acco/statistics.html', context)
