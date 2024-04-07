from .getPublicData import getAllCars
import json
import time

def getCircleData():
    cars = list(getAllCars())
    oilData = []
    electricData = []
    for i in cars:
        if i.energyTpye == '汽油':
            oilData.append([i.carName,i.salVolume,i.energyTpye])
        elif i.energyTpye == '纯电动':
            electricData.append([i.carName,i.salVolume,i.energyTpye])

    oilData = oilData[:10]
    electricData = electricData[:10]
    return oilData,electricData
