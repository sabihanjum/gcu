from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        try:
            n1 = int(request.POST.get('num1', '0'))
            n2 = int(request.POST.get('num2', '0'))
        except (ValueError, TypeError):
            return render(request, 'index.html', {'error': 'Please enter valid integers.'})

        res = n1 + n2
        return render(request, 'index.html', {'n1': n1, 'n2': n2, 'res': res})
    return render(request, 'index.html')


def loop(request):
    if request.method == 'POST':
        num = int(request.POST.get('num'))
        data = {
            'list': list(range(1, num + 1))
        }
        return render(request, 'loop.html', data)
    else:
        return render(request, 'loop.html')