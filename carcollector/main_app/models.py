from django.db import models
from django.urls import reverse
from datetime import date

SERVICES = (
    ('M', 'Maintenance'),
    ('R', 'Repair'),
    ('C', 'Cleaning'),
)

class Accessory(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('accessories_detail', kwargs={'pk': self.id})


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")
    accessories = models.ManyToManyField(Accessory)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"car_id": self.id})
    
    def __str__(self):
        return self.name
    
    def serviced_today(self):
        return self.service_set.filter(date=date.today()).count() >= len(SERVICES)

class Service(models.Model):
    date = models.DateField()
    service_type = models.CharField(max_length=1, choices=SERVICES, default=SERVICES[0][0])
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.car.name} {self.get_service_type_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']