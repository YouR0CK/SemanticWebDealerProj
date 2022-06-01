from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Dealer, Employee, Engine, Car
from .serializers import DealerSerializer, EmployeeSerializer, EngineSerializer, CarSerializer

#Dealer Views
class DealerCreationView(generics.CreateAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


class DealerUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = DealerSerializer
    queryset = Dealer.objects.all()


class DealerRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = DealerSerializer
    queryset = Dealer.objects.all()


class DealerListView(generics.ListAPIView):
    serializer_class = DealerSerializer
    queryset = Dealer.objects.all()


class DealerDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = DealerSerializer
    queryset = Dealer.objects.all()


#Employee Views
class EmployeeCreationView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


#Engine Views
class EngineCreationView(generics.CreateAPIView):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer


class EngineUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = EngineSerializer
    queryset = Engine.objects.all()


class EngineRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = EngineSerializer
    queryset = Engine.objects.all()


class EngineListView(generics.ListAPIView):
    serializer_class = EngineSerializer
    queryset = Engine.objects.all()


class EngineDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = EngineSerializer
    queryset = Engine.objects.all()
    

#Car Views
class CarCreationView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarListView(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = CarSerializer
    queryset = Car.objects.all()
