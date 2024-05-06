from django.shortcuts import render, redirect
from .models import Flinch
from .forms import FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect


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
  feeding_form = FeedingForm()
  return render(request, 'flinch/details.html', { 'flinch': flinch, 'feeding_form': feeding_form })

class FlinchCreate(CreateView):
  model = Flinch
  success_url = '/flinch/{id}'
  fields = '__all__'

class FlinchUpdate(UpdateView):
    model = Flinch
    success_url = '/flinch/{id}'
    fields = ['breed', 'description', 'age']

class FlinchDelete(DeleteView):
    model = Flinch
    success_url = '/flinch'
# Path: main_app/views.py

def add_feeding(request, flinch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the flinch_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.flinch_id = flinch_id
    new_feeding.save()
  return redirect('detail', flinch_id=flinch_id)
