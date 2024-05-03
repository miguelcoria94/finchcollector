from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html' , {'author': 'Your Name'})

def flinch_index(request):
    return render(request, 'flinch/index.html'
    , {'cats': ['Luna', 'Cricket', 'Pumpkin']})