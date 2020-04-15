from django.shortcuts import render, redirect
from .models import Book, Author

def createbook(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, 'books.html', context)
def createauthor(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, 'authors.html', context)
def addbook(request):
    if request.method == "POST":
        Book.objects.create(
            title = request.POST['title'],
            description = request.POST['description']
        )
    return redirect('/')
def addauthor(request):
    if request.method == "POST":
        Author.objects.create(
            name = request.POST['name'],
            notes = request.POST['notes']
        )
    return redirect('/author')
def displaybook(request,id):
    context = {
        "book": Book.objects.get(id=id),
        "all_authors": Author.objects.all()
    }
    return render(request, 'book_info.html', context)
def displayauthor(request,id):
    context = {
        'author': Author.objects.get(id=id)
    }

    return render(request, 'author_info.html', context)
def connectauthor(request, id):
    book = Book.objects.get(id=id)
    author = Author.objects.get(id=request.POST['authors'])
    author.books.add(book)
    return redirect(f'/book/info/{id}')
def connectbook(request):

    return redirect('author/info/<int:id>')

# Create your views here.
