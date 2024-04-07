from myApp.models import *

def getAllCars():
    cars = CarInfo.objects.all()
    return cars