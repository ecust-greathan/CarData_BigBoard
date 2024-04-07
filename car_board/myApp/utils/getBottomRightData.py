from .getPublicData import getAllCars
import json
import time
import re

def getRankData():
    cars = list(getAllCars())
    carData = []
    for car in cars:
        car.price = re.findall('\d+\.\d+', car.price)
        car.price = '-'.join(car.price)
        carData.append({
            'brand':car.brand,
            'rank':car.rank,
            'carName':car.carName,
            'carImg':car.carImg,
            'manufacturer':car.manufacturer,
            'carModel':car.carModel,
            'price':car.price,
            'salVolume':car.salVolume,
            'marketTime':car.marketTime,
            'insure':car.insure,
        })
    return carData