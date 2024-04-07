import requests
from lxml import etree
import csv
import os
import time
import json
import pandas as pd
import re
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_board.settings')
django.setup()
from myApp.models import CarInfo,User

class spider(object):
    def __init__(self):
        self.spiderUrl = 'https://www.dongchedi.com/motor/pc/car/rank_data?aid=1839&app_name=auto_web_pc&city_name=%E4%B8%8A%E6%B5%B7&count=10&month=&new_energy_type=&rank_data_type=11&brand_id=&price=&manufacturer=&outter_detail_type=&nation=0'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }
    def init(self):
        if not os.path.exists('./temp.csv'):
            with open('./temp.csv', 'a', newline='', encoding='utf-8') as wf:
                writer = csv.writer(wf)
                writer.writerow(['brand', 'carName', 'carImg', 'saleVolume','price','manufacturer','rank','carModel','energyType','marketTime','insure'])
    # 获取值
    def get_page(self):
        with open('./spiderPage.txt','r') as r_f:
            return r_f.readlines()[-1].strip()

    # 设置值
    def set_page(self,newPage):
        with open('./spiderPage.txt','a') as a_f:
            a_f.write('\n'+str(newPage))

    def main(self):
        count = self.get_page()
        params ={
            'offset':int(count)
        }
        print("数据从{}开始爬取".format(int(count)+1))
        pageJson = requests.get(self.spiderUrl, headers=self.headers,params=params).json()
        pageJson = pageJson['data']['list']
        try:
            for index,car in enumerate(pageJson):
                carData = []
                print("正在爬取第{}条数据".format(index+1))
                carData.append(car['brand_name'])
                carData.append(car['series_name']) #车名
                carData.append(car['image']) #图片
                carData.append(car['count']) #销量
                #价格
                price = []
                price.append(car["min_price"])
                price.append(car["max_price"])
                carData.append(price)
                carData.append(car['sub_brand_name']) # 厂商
                carData.append(car['rank']) # 排名

                #第二个页面
                carNumber = car["series_id"]
                infoHTML = requests.get('https://www.dongchedi.com/auto/params-carIds-x-%s'%carNumber,headers=self.headers)
                infoHTMLpath = etree.HTML(infoHTML.text)
                carModel = infoHTMLpath.xpath("//div[@data-row-anchor='jb']/div[2]/div/text()")[0] # 车型
                carData.append(carModel)
                energyTpye = infoHTMLpath.xpath("//div[@data-row-anchor='fuel_form']/div[2]/div/text()")[0] # 车型
                carData.append(energyTpye)
                marketTime = infoHTMLpath.xpath("//div[@data-row-anchor='market_time']/div[2]/div/text()")[0] # 车型
                carData.append(marketTime)
                insure = infoHTMLpath.xpath("//div[@data-row-anchor='period']/div[2]/div/text()")[0] # 车型
                carData.append(insure)
                print(carData)
                self.save_to_csv(carData)
        except:
            pass

        self.set_page(int(count)+10)
        self.main()
    def save_to_csv(self,resultData):
        with open('temp.csv', 'a', newline='', encoding='utf-8')as f:
            writer =  csv.writer(f)
            writer.writerow(resultData)

    def clear_csv(self):
        df = pd.read_csv('temp.csv',encoding='utf-8')
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)
        print("总数量为%d"%df.shape[0])
        return df.values

    def save_to_sql(self):
        data = self.clear_csv()
        for car in data:
            CarInfo.objects.create(
                brand = car[0],
                carName = car[1],
                carImg = car[2],
                salVolume = car[3],
                price = car[4],
                manufacturer = car[5],
                rank = car[6],
                carModel = car[7],
                energyTpye = car[8],
                marketTime = car[9],
                insure = car[10]
            )


if __name__ == '__main__':
    spiderObj = spider()
    # spiderObj.init()
    # spiderObj.main()
    spiderObj.save_to_sql()