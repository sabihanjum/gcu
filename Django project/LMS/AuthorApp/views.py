from django.shortcuts import render, redirect, get_object_or_404
from .models import Author

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author/list.html', {'authors': authors})

def author_add(request):
    if request.method == 'POST':
        Author.objects.create(
            AuthorName=request.POST.get('AuthorName'),
            AuthorAge=int(request.POST.get('AuthorAge') or 0),
            AuthorPhone=request.POST.get('AuthorPhone') or '',
            AuthorEmail=request.POST.get('AuthorEmail') or '',
        )
        return redirect('author:list')
    return render(request, 'author/add.html')

def author_edit(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == 'POST':
        author.AuthorName = request.POST.get('AuthorName')
        author.AuthorAge = int(request.POST.get('AuthorAge') or 0)
        author.AuthorPhone = request.POST.get('AuthorPhone') or ''
        author.AuthorEmail = request.POST.get('AuthorEmail') or ''
        author.save()
        return redirect('author:list')
    return render(request, 'author/edit.html', {'author': author})

def author_delete(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == 'POST':
        author.delete()
        return redirect('author:list')
    return render(request, 'author/delete_confirm.html', {'author': author})