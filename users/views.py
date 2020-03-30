from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user"""
    print("Made it here in the register pathway")
    if request.method != 'POST':
        #Display blank registration form
        form = UserCreationForm()
    else:
        #Process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Log the user in and then redirect to home page
            login(request, new_user)
            return redirect('learning_logs:index')

    #Display a blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def login(request):
    """Login page"""
    print("Made it here in login")
    return render(request, 'registration/login.html')

def logout(request):
    """Logout page"""
    print("Made it here")
    return render(request, 'registration/logout.html')

