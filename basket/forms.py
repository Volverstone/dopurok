from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'cart_number', 'phone_number']
        widgets = {
            'card_number': forms.TextInput(attrs={'maxlength': 16}),
            'phone_number': forms.TextInput(attrs={'maxlength': 20}),
        }

