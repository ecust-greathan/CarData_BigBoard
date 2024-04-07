from .getPublicData import getAllCars
import json
import time

def getPriceSortData():
    cars = list(getAllCars())
    priceSortList ={'0-5w':0,'5w-10w':0,'10w-20w':0,'20w-30w':0,'30w以上':0}
    for i in cars:
        s=[json.loads(i.price)[0]][0]
        if s<5:
            priceSortList['0-5w']+=1
        elif s>=5 and s<10:
            priceSortList['5w-10w']+=1
        elif s>=10 and s<20:
            priceSortList['10w-20w']+=1
        elif s>=20 and s<30:
            priceSortList['20w-30w']+=1
        else:
            priceSortList['30w以上']+=1
    realData = []
    for k,v in priceSortList.items():
        realData.append({'name':k,'value':v})

    return realData