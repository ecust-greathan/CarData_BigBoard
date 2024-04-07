from django.db import models

class CarInfo(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(verbose_name='品牌',max_length=255,default='')
    carName = models.CharField(verbose_name='车名',max_length=255,default='')
    carImg = models.CharField(verbose_name='图片',max_length=255,default='')
    salVolume = models.CharField(verbose_name='销量',max_length=255,default='')
    price = models.CharField(verbose_name='价格',max_length=255,default='')
    manufacturer = models.CharField(verbose_name='厂商',max_length=255,default='')
    rank = models.CharField(verbose_name='排名',max_length=255,default='')
    carModel = models.CharField(verbose_name='车型',max_length=255,default='')
    energyTpye = models.CharField(verbose_name='能源类型',max_length=255,default='')
    marketTime = models.CharField(verbose_name='上市时间',max_length=255,default='')
    insure = models.CharField(verbose_name='保修时间',max_length=255,default='')
    createTime = models.DateField(verbose_name='创建时间',auto_now_add=True)
    class Meta:
        db_table = 'carInfo'

#用户表
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(verbose_name='用户名',max_length=255,default='')
    password = models.CharField(verbose_name='密码',max_length=255,default='')
    createTime = models.DateField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        db_table = 'user'