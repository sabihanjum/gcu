# ...existing code...
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Groom

def home(request):
    # ...existing home code...
    return render(request, 'groom/home.html')

def add(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        age = request.POST.get('age')

        g = Groom()
        g.name = name
        g.phone = phone
        g.email = email
        g.age = age
        g.save()
        # return HttpResponse("Groom added successfully")
        return redirect('groom:display')
    else:


        # render same template with submitted data
        return render(request, 'groom/add.html')

    # GET — show empty form
    # return render(request, 'groom/add.html')
def display(request):
    grooms = Groom.objects.all()
    data = {'groom_list': grooms}
    return render(request, 'groom/groomlist.html', data)
# ...existing code...