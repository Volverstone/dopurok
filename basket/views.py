from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem
from .forms import OrderForm
from books.models import Book

def card_add(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    cart = request.session.get('cart', [])
    cart.append(book.id)
    request.session['cart'] = cart
    return redirect('cart_detail')

def card_detail(request):
    cart = request.session.get('cart', [])
    books = Book.objects.filter(pk__in=cart)
    return render(request, 'basket/card_detail.html', {'books': books})

def card_remove(request, book_id):
    cart= request.session.get('cart', [])
    if book_id in cart:
        cart.remove(book_id)
    request.session['cart'] = cart
    return redirect('cart_detail')

def create_order(request):
    cart = request.session.get('cart', [])
    books = Book.objects.filter(id__in=cart)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for book in books:
                OrderItem.objects.create(order=order, book=book)
            request.session['cart'] = []
            return redirect('order_list')
    else:
        form = OrderForm()

    return render(request, 'basket/create_order.html', {'form': form, 'books': books})

def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'basket/order_list.html', {'orders': orders})

def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.delete()
    return redirect('order_list')