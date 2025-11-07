# ...existing code...
from django.shortcuts import render

def home(request):
    # ...existing home code...
    return render(request, 'groom/home.html')

def add(request):
    groom = None
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        age = request.POST.get('age', '').strip()

        groom = {
            'name': name,
            'phone': phone,
            'email': email,
            'age': age,
        }

        # render same template with submitted data
        return render(request, 'groom/add.html', {'groom': groom})

    # GET — show empty form
    return render(request, 'groom/add.html')
# ...existing code...