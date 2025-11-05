# create function for home page

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Calculator App")

def about(request):
    return HttpResponse("This is a simple calculator application built with Django.")

def contact(request):
    return HttpResponse("Contact us")

def add(request):
    a = int(request.GET.get('a', 0))
    b = int(request.GET.get('b', 0))
    result = a + b
    return HttpResponse(f"The sum of {a} and {b} is {result}")