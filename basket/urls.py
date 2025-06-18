from django.urls import path
from . import views

urlpatterns = [
    path('cart/add/<int:book_id>/', views.card_add, name='cart_add'),
    path('cart/', views.card_detail, name='cart_detail'),
    path('cart/remove/<int:book_id>/', views.card_remove, name='cart_remove'),
    path('order/create/', views.create_order, name='create_order'),
    path('orders/', views.order_list, name='order_list'),
    path('order/delete/<int:order_id>/', views.order_delete, name='order_delete'),
]