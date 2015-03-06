from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the index page!")

def about(request):
    return HttpResponse("Welcome to the about page!")

def contact(request):
    return HttpResponse("Welcome to the contact page!")

def why(request):
    return HttpResponse("Welcome to the why page!")
