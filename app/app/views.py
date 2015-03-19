from django.shortcuts import render
from inventory.forms import UserForm

def index(request):
    return render(request, 'app/index.html', {})

def about(request):
    return render(request, 'app/about.html', {})

def contact(request):
    return render(request, 'app/contact.html', {})

def why(request):
    return render(request, 'app/why.html', {})

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()

    return render(request, 'app/register.html', {'user_form': user_form, 'registered': registered} )
