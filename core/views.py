from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            print("User")
            return redirect('dashboard')  # Replace 'dashboard' with your desired URL name
        else:
            print("UserNot")
            error_message = "Invalid username or password"
    else:
        error_message = ""

    return render(request, 'accounts/autorization/login.html', {'error_message': error_message})
