from django import forms
from .models import Reviews
from django.core.validators import MaxValueValidator

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['text', 'mark']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
            'mark': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }