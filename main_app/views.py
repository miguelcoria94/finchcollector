from django.shortcuts import render, redirect
from .models import Flinch
from .forms import FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Toy
from django.views.generic import ListView, DetailView


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
  id_list = flinch.toys.all().values_list('id')
  toys_that_flinch_doesnt_have = Toy.objects.exclude(id__in=id_list)
  return render(request, 'flinch/details.html', { 'flinch': flinch, 'feeding_form': feeding_form, 'toys': toys_that_flinch_doesnt_have})

def assoc_toy(request, flinch_id, toy_id):
  Flinch.objects.get(id=flinch_id).toys.add(toy_id)
  return redirect('detail', flinch_id=flinch_id)

def unassoc_toy(request, flinch_id, toy_id):
  Flinch.objects.get(id=flinch_id).toys.remove(toy_id)
  return redirect('detail', flinch_id=flinch_id)

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


class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'