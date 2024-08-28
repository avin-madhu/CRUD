from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import admin
from .models import Book
from .forms import BookForm

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

# add books
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            print("done")
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form':form})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        print("deleted!")
        return redirect('book_list')
    return render(request, 'confirm_delete.html', {"book": book})
    







