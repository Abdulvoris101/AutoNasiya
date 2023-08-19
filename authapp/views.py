from django.shortcuts import render, redirect
from .forms import ProductPurchaseForm, LoginForm, ChangePasswordForm
from django.views.generic.edit import FormView
from .models import Customer
import shortuuid
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

class CustomerCreateView(FormView):
    template_name = "accounts/customerCreate.html"
    success_url = "account/"
    form_class  = ProductPurchaseForm
    
    def form_valid(self, form):
        password = shortuuid.uuid()

        customer = Customer(
            firstName=form.cleaned_data['firstName'],
            phoneNumber=form.cleaned_data['phoneNumber'],
            showedPassword=password
        )

        customer.set_password(password)
        customer.save()

        product_purchase = form.save(commit=False)
        product_purchase.customer = customer
        product_purchase.save()

        return super().form_valid(form)


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, "accounts/authorization/login.html", {'form': form})


    def post(self, request):
        form = LoginForm(request.POST)
        
        if form.is_valid():
            phoneNumber = form.cleaned_data['phoneNumber']
            password = form.cleaned_data['password']
            user = authenticate(request, phoneNumber=phoneNumber, password=password)

            if user:
                login(request, user)
                if not user.is_staff:
                    return redirect('product', pk=user.purchases.first().id)
                
                
                return redirect('index')

            messages.error(request, "Telefon nomer yoki password no'tog'ri!" )
            
        
        return render(request, "accounts/authorization/login.html", {'form': form})


class ChangePassword(View):
    def get(self, request):
        form = ChangePasswordForm()
        return render(request, "accounts/authorization/changePassword.html", {'form': form})
        
    def post(self, request):
        form = ChangePasswordForm(request.POST)
        
        if form.is_valid():
            oldPassword = form.cleaned_data['oldPassword']
            password = form.cleaned_data['password']
            print(request.user)
            user = Customer.objects.get(phoneNumber=request.user)
            
            if user.check_password(oldPassword):
                user.set_password(password)
                user.save()
                return redirect('index')
            messages.error(request, "Avvalgi parol bunday emas!" )
            
        return render(request, "accounts/authorization/changePassword.html", {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")