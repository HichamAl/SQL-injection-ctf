from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db import connection
from django.db import ProgrammingError

# SQL CTF GET THE FLAG
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
        return render(request, 'ctf/home.html', {'columns': columns, 'results': results, 'error_message': error_message})
    return render(request, 'ctf/home.html')


# SQL CTF VIEW LOGIN BYPASS
def sql(request):
    if request.method == 'POST':
        # Get the form data from the POST request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Execute the SQL query
        try:
            if username is not None and password is not None:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM auth_user WHERE username = '" + username + "' AND password = '" + password + "'")
                    row = cursor.fetchone()
        except:
            error_message = "Error executing SQL query"
            return render(request, 'ctf/ctf.html', {'error_message': error_message})

        # Authenticate the user's credentials
        if row is not None:
            user = User(id=row[0], username=row[1], password=row[2])
            # Credentials are valid
            return render(request, 'ctf/home.html')
        else:
            # Credentials are invalid
            return render(request, 'ctf/ctf.html')
    else:        
        return render(request, 'ctf/ctf.html')

