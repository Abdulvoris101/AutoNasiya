from django import forms

from .models import ProductPurchase

# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         exclude = ("password", )
        
#         widgets = {
#             "checkId": forms.TextInput(attrs={
#                 "placeholder": "CheckId",
#                 "class": "form-control",
#             }),
#             "firstName": forms.TextInput(attrs={
#                 "placeholder": "Ism",
#                 "class": "form-control",
#             }),
#             "phoneNumber": forms.TextInput(attrs={
#                 "placeholder": "Tel.raqam",
#                 "class": "form-control",
#             })
#         }

    

class ProductPurchaseForm(forms.ModelForm):
    class Meta:
        model = ProductPurchase
        exclude = ("customer", "amountOfMonth", "nextPaymentAmount", "totalPrice", "status", "finishedAt")


    firstName = forms.CharField(label="Ism", max_length=255, widget=forms.TextInput(attrs={
        "placeholder": "Ism",
        "class": "form-control",
    }))
    phoneNumber = forms.CharField(label="Tel.raqam", max_length=255, widget=forms.TextInput(attrs={
        "placeholder": "Tel.raqam",
        "class": "form-control",
    }))