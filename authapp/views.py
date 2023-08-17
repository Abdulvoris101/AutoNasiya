from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from .forms import ProductPurchaseForm
from django.views.generic.edit import FormView
from .models import Customer, ProductPurchase
import shortuuid


def index(request):
    customer = Customer.objects.all()
    return render(request, "index.html",  {'customer': customer})




class CustomerCreateView(FormView):
    template_name = "accounts/customerCreate.html"
    success_url = "/"
    form_class  = ProductPurchaseForm

    def form_valid(self, form):
        # Create the customer

        customer = Customer.objects.create(
            firstName=form.cleaned_data['firstName'],
            phoneNumber=form.cleaned_data['phoneNumber'],
            password=shortuuid.uuid(),  # You need to set the password here
        )

        # Create the product purchase
        product_purchase = form.save(commit=False)
        product_purchase.customer = customer
        product_purchase.save()

        return super().form_valid(form)


def customerDetail(request, item_id):
    
    items = ProductPurchase.objects.filter(pk=item_id)

    context = {
        'items': items
    }
    return render(request, "accounts/customerDetail.html", context)
