from django.shortcuts import render
from django.http import HttpResponse

def lsn_4(request):
    return HttpResponse('домашка за 4 занятие')

def start(request):
    return HttpResponse('введите адрес "lesson_4/"')

# Create your views here.
