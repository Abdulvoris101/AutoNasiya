from django import forms

from .models import ProductPurchase
    

class ProductPurchaseForm(forms.ModelForm):
    class Meta:
        model = ProductPurchase
        exclude = ("customer", "amountOfMonth", "nextPaymentAmount", "totalPrice", "status", "finishedAt")
        fields=['firstName', 'phoneNumber', 'productName', 'costProduct', 'duration', 'taxRate', 'startingFee', 'startedAt',]
        
        
    firstName = forms.CharField(label="Ism", max_length=255, widget=forms.TextInput(attrs={
        "placeholder": "Ism",
        "class": "form-control",
    }))
    phoneNumber = forms.CharField(label="Tel", max_length=255, widget=forms.NumberInput(attrs={
        "placeholder": "+998",
        "class": "form-control",
    }))
    
    productName = forms.CharField(label="Mahsulot", widget=forms.TextInput(attrs={
        "placeholder": "Nomi",
        "class": "form-control",
    }))
    
    costProduct = forms.FloatField(label="Maxsulot tan", widget=forms.NumberInput(attrs={
        "placeholder": "narxi",
        "class": "form-control",
    }))
    
    
    startingFee = forms.IntegerField(label="Boshlang'ich", widget=forms.NumberInput(attrs={
        "placeholder": "to'lov",
        "class": "form-control",
    }))
    
    taxRate = forms.IntegerField(label="Soliq", widget=forms.NumberInput(attrs={
        "placeholder": "foizi",
        "class": "form-control",
    }))
    
    duration = forms.IntegerField(label="Necha oyga", widget=forms.NumberInput(attrs={
        "placeholder": "davomiyligi",
        "class": "form-control",
    }))
    
    startedAt = forms.DateTimeField(label="Start", input_formats=['%Y-%m-%d %H:%M:%S'], widget=forms.DateInput(attrs={
        'type': 'date',
        "class": "form-control",
    }))


class LoginForm(forms.Form):
    phoneNumber = forms.CharField(max_length=255)
    password = forms.CharField(max_length=500   , widget=forms.PasswordInput)
    
    phoneNumber = forms.IntegerField(label="Tel raqam", widget=forms.NumberInput(attrs={
        "placeholder": "+998",
        "class": "form-control",
    }))
    
    password = forms.CharField(label="parol", widget=forms.TextInput(attrs={
        "placeholder": "password",
        "class": "form-control",
    }))
    
    
class ChangePasswordForm(forms.Form):
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    oldPassword = forms.CharField(max_length=500, widget=forms.PasswordInput)
    
 