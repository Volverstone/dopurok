from django.db import models
from django.contrib.auth.models import User
from books.models import Book

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    cart_number = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Заказ номер{self.id} от {self.full_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book.title} в заказе номер {self.order.id}'