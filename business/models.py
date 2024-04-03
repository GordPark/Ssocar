from django.db import models

# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=100)
    def __str__(self):
        return self.car_name

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)

class Rental(models.Model):
    car_name = models.ForeignKey(Car, on_delete=models.CASCADE)
    Customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rental_date = models.DateTimeField("rental date")
    price = models.IntegerField()

