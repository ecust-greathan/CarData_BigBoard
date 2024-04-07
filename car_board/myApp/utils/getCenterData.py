from .getPublicData import getAllCars
import json
import time

def getBaseData():
    cars = getAllCars()
    sumCar = len(cars)
    highVolume = cars[0].salVolume
    topCar = cars[0].carName
    # 获取最高销量的车型
    carModels = {}
    maxModel = 0
    mostModel = ""
    for i in cars:
        if carModels.get(i.carModel,-1) == -1:
            carModels[str(i.carModel)] =1
        else:
            carModels[str(i.carModel)] += 1

    carModels = sorted(carModels.items(),key=lambda x:x[1],reverse=True) #获取到车型
    mostModel = carModels[0][0]
    #上榜车辆最多的品牌
    carBrands = {}
    maxBrand = 0
    mostBrand = ""
    for i in cars:
        if carBrands.get(i.brand,-1) == -1:
            carBrands[str(i.brand)] =1
        else:
            carBrands[str(i.brand)] += 1

    for k,v in carBrands.items():
        if v > maxBrand:
            maxBrand = v
            mostBrand = k

    #平均价格
    carPrices = {}
    averagePrice = 0
    sumPrice = 0
    for i in cars:
        x = json.loads(i.price)[0] + json.loads(i.price)[1]
        sumPrice += x
    averagePrice = sumPrice / (sumCar*2)
    averagePrice = round(averagePrice,2)
    return sumCar,highVolume,topCar,mostModel,mostBrand,averagePrice


def getRollData():
    cars = list(getAllCars())
    #品牌
    carBrands = {}
    for i in cars:
        if carBrands.get(i.brand,-1) == -1:
            carBrands[str(i.brand)] =1
        else:
            carBrands[str(i.brand)] += 1

    brandList = [(value,key) for key,value in carBrands.items()]
    brandList = sorted(brandList,reverse=True)[:10]
    sortDict = {i[1]:i[0] for i in brandList}
    lastSortList = []
    for k,v in sortDict.items():
        lastSortList.append({
            'name':k,
            'value':v
        })
    return lastSortList

def getTypeRate():
    cars = list(getAllCars())
    # 能源类型
    carTypes = {}
    for i in cars:
        if carTypes.get(i.energyTpye,-1) == -1:
            carTypes[str(i.energyTpye)] = 1
        else:
            carTypes[str(i.energyTpye)] += 1
    oilRate = round(carTypes['汽油'] / (len(cars)) * 100,2)
    electricRate = round(carTypes['纯电动'] / (len(cars)) * 100,2)
    mixRate = round((len(cars)-carTypes['汽油']-carTypes['纯电动']) / (len(cars)) * 100,2)

    return oilRate,electricRate,mixRate

