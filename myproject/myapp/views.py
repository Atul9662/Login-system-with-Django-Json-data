# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import json
from django.urls import reverse


def my_json_view(request):
    data = {
        'message': 'Hello, world!',
        'status': 200,

    }
    return JsonResponse(data)

def signup_page(request):
    return render(request, 'myapp/signup.html')

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Insert user into the database using a raw SQL query
        with connection.cursor() as cursor:
            cursor.execute("SELECT id as count from users where username = %s or email = %s",[username,email])
            res = cursor.fetchone()
            print(res)
            if res:
                return JsonResponse({'message': 'User Already axist!'}, status=201)

            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                           [username, email, password])


        return JsonResponse({'redirect': reverse('login_page')})
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


def login_page(request):
    return render(request, 'myapp/login.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        # Check user credentials using a raw SQL query
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", [username, password])
            user = cursor.fetchone()

        if user:
            return JsonResponse({'message': 'Login successful!',"status":200}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials',"status":200}, status=200)

    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
