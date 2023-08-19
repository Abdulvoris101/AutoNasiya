from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['date', 'amount']
        
    amount = forms.FloatField(label="To'lov", widget=forms.NumberInput(attrs={
        "placeholder": "Miqdori",
        "class": "form-control",
    }))
    
    date = forms.DateTimeField(label="To'lov sanasi", input_formats=['%Y-%m-%d %H:%M:%S'], widget=forms.DateInput(attrs={
        'type': 'date',
        "class": "form-control",
    }))

