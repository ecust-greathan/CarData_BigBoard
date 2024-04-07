from .getPublicData import getAllCars
import json
import time
import re

#柱状图数据
def getSquareData():
    cars = getAllCars()
    carsVolume = {}
    for i in cars:
        if carsVolume.get(i.carName,-1) == -1:
            carsVolume[i.carName] = int(i.salVolume)
        else:
            carsVolume[i.carName] += int(i.salVolume)
    carsVolume = sorted(carsVolume.items(),key=lambda x:x[1],reverse=True)[:16]
    CarNameList = []
    volumeList = []
    priceList = []
    for i in carsVolume:
        CarNameList.append(i[0])
        volumeList.append(i[1])
    for j in cars[:12]:
        j.price = re.findall('\d+\.\d+',j.price)
        j.price = j.price[0]
        priceList.append(float(j.price))

    return CarNameList,volumeList,priceList

