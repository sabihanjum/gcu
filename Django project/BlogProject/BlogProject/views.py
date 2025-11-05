from django.http import HttpResponse

def list(request):
    return HttpResponse("All posts will be displayed here.")

def new(request):
    return HttpResponse("Create a new post here.")