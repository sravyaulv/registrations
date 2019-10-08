from django.shortcuts import render
from django.http import HttpResponse
from .models import insert_user, fetch_data
# Create your views here.

def home(request):
    return render(request, 'home.html')

def insert(request):
    name = request.GET['name']
    age = request.GET['age']
    dob = request.GET['dob']
    insert_user(age, name, dob)

    return render(request, 'success.html')

def fetch_all_data(request):
    data = fetch_data()
    return render(request, 'viewData.html', {'data': data})

