from django.shortcuts import render, redirect
from .models import Car, Accessory
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import ServiceForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CarUpdate(LoginRequiredMixin, UpdateView):
    model = Car
    fields = ['brand', 'description', 'year', 'image']

class CarDelete(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = reverse_lazy('cars_index')

class AccessoryList(LoginRequiredMixin, ListView):
    model = Accessory

class AccessoryDetail(LoginRequiredMixin, DetailView):
    model = Accessory

class AccessoryCreate(LoginRequiredMixin, CreateView):
    model = Accessory
    fields = ['name', 'type', 'price']

class AccessoryUpdate(LoginRequiredMixin, UpdateView):
    model = Accessory
    fields = ['name', 'type', 'price']

class AccessoryDelete(LoginRequiredMixin, DeleteView):
    model = Accessory
    success_url = reverse_lazy('accessories_index')

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def cars_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', {'cars': cars})

@login_required
def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    service_form = ServiceForm()
    accessories_car_doesnt_have = Accessory.objects.exclude(id__in=car.accessories.all().values_list('id'))
    return render(request, 'cars/detail.html', {
        'car': car,
        'service_form': service_form,
        'accessories': accessories_car_doesnt_have,
    })

@login_required
def add_service(request, car_id):
    form = ServiceForm(request.POST)
    if form.is_valid():
        new_service = form.save(commit=False)
        new_service.car_id = car_id
        new_service.save()
    return redirect('detail', car_id=car_id)

@login_required
def assoc_accessory(request, car_id, accessory_id):
    Car.objects.get(id=car_id).accessories.add(accessory_id)
    return redirect('detail', car_id=car_id)

@login_required
def unassoc_accessory(request, car_id, accessory_id):
    Car.objects.get(id=car_id).accessories.remove(accessory_id)
    return redirect('detail', car_id=car_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
            
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)