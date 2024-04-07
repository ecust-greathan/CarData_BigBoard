import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image
from pymysql import *
import json

def get_img(field,targetImageSrc,resImageSrc):
    con = connect(host='localhost', user='root', password='123456', db='cardata', charset='utf8mb4')
    cursor = con.cursor()
    sql = f"select {field} from carinfo"
    cursor.execute(sql)
    data = cursor.fetchall()

    text = ''
    for i in data:
        if i[0] != '':
            tahArr = i
            for j in tahArr:
                text += j

    cursor.close()
    con.close()
    data_cut = jieba.cut(text, cut_all=False)
    string = ' '.join(data_cut)

    #图片
    img = Image.open(targetImageSrc)
    img_array = np.array(img)
    wd = WordCloud(font_path='STHUPO.TTF',background_color='#04122c',mask=img_array,width=1000,height=860)
    wd.generate_from_text(string)
    #绘制图片
    fig = plt.figure(1)
    plt.imshow(wd)
    plt.axis('off')
    plt.savefig(resImageSrc,dpi=800,bbox_inches='tight',pad_inches=-0.1)

get_img('manufacturer','./car1.png','./CarCloud.png')