from django.shortcuts import render
from .models import Flinch

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html' , {'author': 'Your Name'})

def flinch_index(request):
    finches = Flinch.objects.all()
    return render(request, 'flinch/index.html', { 'flinches': finches})

def flinch_detail(request, flinch_id):
  flinch = Flinch.objects.get(id=flinch_id)
  return render(request, 'flinch/detail.html', { 'flinch': flinch })