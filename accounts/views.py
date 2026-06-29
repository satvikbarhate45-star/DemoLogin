from django.shortcuts import render, redirect
from .models import Registration


def register(request):
    if request.method == 'POST':
        Registration.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            password=request.POST.get('password')
        )
        return redirect('login')

    return render(request, 'accounts/register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Registration.objects.filter(
            email=email,
            password=password
        ).first()

        if user:
            return render(request, 'accounts/home.html', {'user': user})

        return render(
            request,
            'accounts/login.html',
            {'message': 'Invalid Email or Password'}
        )

    return render(request, 'accounts/login.html')


def home(request):
    return render(request, 'accounts/home.html')