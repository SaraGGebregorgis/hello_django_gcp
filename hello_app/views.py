from django.shortcuts import render, HttpResponse

def hello(request):
    return HttpResponse('Hello! This is a Django app on GCP!!!') 
