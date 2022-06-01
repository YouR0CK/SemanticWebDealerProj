from django.db import models
from django.forms import CharField, IntegerField

class Dealer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    salary = models.IntegerField()
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class Engine(models.Model):
    index = models.CharField(max_length=20)    
    fuel = models.CharField(max_length=10)
    power = models.IntegerField()
    torque = models.IntegerField()
    consumption = models.IntegerField()

    def __str__(self):
        return self.index

class Car(models.Model):
    vendor = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    dealer = models.ManyToManyField(Dealer)
    doorscnt = models.IntegerField()
    engine = models.ManyToManyField(Engine)
    
    def __str__(self):
        return f'{self.vendor} {self.model}'    