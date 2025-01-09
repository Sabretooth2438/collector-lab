from django.shortcuts import render, redirect
from .models import Car
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ServiceForm
from django.urls import reverse_lazy

class CarCreate(CreateView):
    model = Car
    fields = '__all__'

class CarUpdate(UpdateView):
    model = Car
    fields = ['brand', 'description', 'year', 'image']

class CarDelete(DeleteView):
    model = Car
    success_url = reverse_lazy('cars_index')

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    service_form = ServiceForm()
    return render(request, 'cars/detail.html', {'car': car,'service_form': service_form })

def add_service(request, car_id):
    form = ServiceForm(request.POST)
    if form.is_valid():
        new_service = form.save(commit=False)
        new_service.car_id = car_id
        new_service.save()
    return redirect('detail', car_id=car_id)