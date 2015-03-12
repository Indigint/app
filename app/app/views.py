from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html', {})

def about(request):
    return render(request, 'app/about.html', {})

def contact(request):
    return render(request, 'app/contact.html', {})

def why(request):
    return render(request, 'app/why.html', {})
