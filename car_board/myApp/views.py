from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils.getCenterData import getBaseData,getRollData,getTypeRate
from .utils.getCenterLeftData import getPieBrandData
from .utils.getBottomLeftData import getSquareData
from .utils.getCenterRightData import getPriceSortData
from .utils.getCenterChangeData import getCircleData
from .utils.getBottomRightData import getRankData

class center(APIView):
    def get(self,request):
        sumCar,highVolume,topCar,mostModel,mostBrand,averagePrice = getBaseData()
        RollData = getRollData()
        oilRate,electricRate,mixRate = getTypeRate()
        # 构建响应数据
        content = {
            "success": True,
            "code": 1000,
            "data": {
                "sumCar": sumCar,
                "highVolume": highVolume,
                "topCar": topCar,
                "mostModel": mostModel,
                "mostBrand": mostBrand,
                "averagePrice": averagePrice,
                'rollData':RollData,
                'oilRate':oilRate,
                'electricRate':electricRate,
                'mixRate':mixRate
            },
            "message": "中部信息获取成功"
        }
        return Response(content)

class centerLeft(APIView):
    def get(self,request):
        lastPieList = getPieBrandData()
        # 构建响应数据
        content = {
            "success": True,
            "code": 1000,
            "data": {
                'lastPieList':lastPieList
            },
            "message": "左部饼图信息获取成功"
        }
        return Response(content)

class bottomLeft(APIView):
    def get(self, request):
        CarNameList,volumeList,priceList = getSquareData()
        # 构建响应数据
        content = {
            "success": True,
            "code": 1000,
            "data": {
                'CarNameList':CarNameList,
                'volumeList':volumeList,
                'priceList':priceList
            },
            "message": "底部柱状图信息获取成功"
        }
        return Response(content)

class centerRight(APIView):
    def get(self,request):
        realData = getPriceSortData()
        # 构建响应数据
        content = {
            "success": True,
            "code": 1000,
            "data": {
                'realData':realData
            },
            "message": "中部右侧信息获取成功"
        }
        return Response(content)

class centerRightChange(APIView):
    def get(self,request,energyType):
        oilData,electricData = getCircleData()
        realData = []
        if energyType == 1:
            realData = oilData
        else:
            realData = electricData
        # 构建响应数据
        content = {
            "success": True,
            "code": 1000,
            "data": {
                'realData':realData
            },
            "message": "中部右侧油车电车切换信息获取成功"
        }
        return Response(content)

class bottomRight(APIView):
    def get(self,request):
        carData = getRankData()
        # 构建响应数据
        content = {
            "success": True,
            "code": 1000,
            "data": {
                'carData':carData
            },
            "message": "底部右侧排行榜信息获取成功"
        }
        return Response(content)