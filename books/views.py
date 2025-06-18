from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Reviews
from django.db.models import Avg
from .forms import ReviewForm
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = Reviews.objects.filter(book=book)
    average_rating = reviews.aggregate(Avg('mark'))['mark__avg']

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.author = request.user
            review.save()

            return redirect('book_detail', pk=pk)
    else:
        form = ReviewForm()

    return render(request, 'books/book_detail.html', {
        'book': book,
        'reviews': reviews,
        'average_rating': average_rating,
        'form': form
    })