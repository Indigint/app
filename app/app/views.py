from django.shortcuts import render
from inventory.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

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

def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                # The account is valid and active
                login(request, user)
                return HttpResponseRedirect('/index/')
            else:
                # Inactive account
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:

        return render(request, 'app/login.html', {})

@login_required
def logout_user(request):
    logout(request)

    return HttpResponseRedirect('/index/')