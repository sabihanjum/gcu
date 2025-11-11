# ...existing code...
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def home(request):
    books = Book.objects.all()
    data = {'books': books}
    return render(request, 'book/index.html', data)

def add(request):
    if request.method == 'POST':
        bookName = request.POST.get('bookName')
        authorName = request.POST.get('authorName')
        publishedDate = request.POST.get('publishedDate')
        ratings = int(request.POST.get('ratings') or 0)
        price = float(request.POST.get('price') or 0)

        Book.objects.create(
            bookName=bookName,
            authorName=authorName,
            publishedDate=publishedDate,
            ratings=ratings,
            price=price
        )
        return redirect('book:home')

    return render(request, 'book/add.html')

def edit(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.bookName = request.POST.get('bookName')
        book.authorName = request.POST.get('authorName')
        book.publishedDate = request.POST.get('publishedDate')
        book.ratings = int(request.POST.get('ratings') or 0)
        book.price = float(request.POST.get('price') or 0)
        book.save()
        return redirect('book:home')

    return render(request, 'book/edit.html', {'book': book})

def delete(request, id):
    book = get_object_or_404(Book, id=id)
    
    book.delete()
    return redirect('book:home')
    
