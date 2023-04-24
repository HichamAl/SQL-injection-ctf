from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import connection
from django.db import ProgrammingError
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .backends import RawSQLBackend

# SQL CTF GET THE FLAG
@login_required
def home(request):
    error_message = None
    if request.method == 'POST':
        query = request.POST.get('query')
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                columns = [col[0] for col in cursor.description]
                results = cursor.fetchall()
        except Exception as e:
            error_message = str(e)
            columns = []
            results = []
        return render(request, 'ctf/home.html', {'columns': columns, 'results': results, 'error_message': error_message })
    return render(request, 'ctf/home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password, backend='ctf.backends.RawSQLBackend')
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password.'
    else:
        error_message = ''
    return render(request, 'ctf/ctf.html', {'error_message': error_message})

