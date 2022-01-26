from http.client import TOO_MANY_REQUESTS
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Create your views here.
from django.http import HttpResponse

from main_app.models import Perch

from .models import Finch
from .forms import FeedingForm

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['species', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    unassociated_perches = Perch.objects.exclude(id__in = finch.perches.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', { 
        'finch': finch, 
        'feeding_form': feeding_form,
        'perches': unassociated_perches
    })

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

class PerchList(ListView):
    model = Perch

class PerchDetail(DetailView):
    model = Perch

class PerchCreate(CreateView):
    model = Perch
    fields = '__all__'

class PerchUpdate(UpdateView):
    model = Perch
    fields = ['name', 'location', 'num_perches']

class PerchDelete(DeleteView):
    model = Perch
    success_url = '/perches/'