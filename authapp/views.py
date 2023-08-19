from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductPurchaseForm
from core.forms import PaymentForm
from django.views.generic.edit import FormView
from .models import Customer, ProductPurchase
from django.db.models import Q
from core.models import Payment
import shortuuid



def index(request):
    customer = Customer.objects.all()

    query = request.GET.get('q')  # Get the search query from the URL parameter
    if query:
        results = Customer.objects.filter(
            Q(firstName__icontains=query) |  # Search by firstName
            Q(phoneNumber__icontains=query) |  # Search by phoneNumber
            Q(checkId__icontains=query)  # Search by checkId
        )
    else:
        results = []

    context = {
        'query': query,
        'results': results,
        'customer': customer
    }
    
    
    return render(request, "index.html", context)


class CustomerCreateView(FormView):
    template_name = "accounts/customerCreate.html"
    success_url = "/"
    form_class  = ProductPurchaseForm
    def form_valid(self, form):
        customer = Customer.objects.create(
            firstName=form.cleaned_data['firstName'],
            phoneNumber=form.cleaned_data['phoneNumber'],
            password=shortuuid.uuid(),
        )
        product_purchase = form.save(commit=False)
        product_purchase.customer = customer
        product_purchase.save()

        return super().form_valid(form)





def customerDetail(request, pk):
    product = ProductPurchase.objects.filter(pk=pk)
        
    item = get_object_or_404(ProductPurchase, pk=pk)
    payment = Payment.objects.filter(productPurchase=item)

    payment_count = payment.count()
    
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.productPurchase = item
            product.save()

            return redirect('index')  # Replace 'index' with your desired URL name
    else:
        form = PaymentForm()

    context = {
        'item': item,
        'payment': payment,
        'form': form,
        'product': product,
        'payment_count' : payment_count
    }
    
    return render(request, "accounts/customerDetail.html", context)



