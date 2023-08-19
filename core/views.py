from core.models import Payment
from core.forms import PaymentForm
from authapp.models import ProductPurchase
from django.shortcuts import get_object_or_404, redirect, render
from authapp.models import Customer
from django.db.models import Q
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    customers = Customer.objects.all()
    
    customer = Customer.objects.get(phoneNumber=request.user)

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
        'customers': customers,
        'customer': customer
    }
    
    return render(request, "index.html", context)


@login_required
def productPurchaseDetail(request, pk):
    product = get_object_or_404(ProductPurchase, pk=pk)
    
    payment = Payment.objects.filter(productPurchase=product)
    
    payment_count = payment.count()
    

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        
        if form.is_valid():
            payment = form.save(commit=False)
            payment.productPurchase = product
            payment.save()

            return redirect('index')  # Replace 'index' with your desired URL name
    else:
        form = PaymentForm()


    context = {
        'payment': payment,
        'form': form,
        'product': product,
        'payment_count' : payment_count
    }
    
    return render(request, "accounts/customerDetail.html", context)

