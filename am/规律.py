# coding:utf-8
import datetime
import io
import os
import re

import oss2
import pymysql
import requests
from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup


# 获取网页内容
# 采集特码 连续7天的数据
def getHTMLText(url):
    headers = {
        "Cookie": "___rl__test__cookies=1668074718832; Hm_lvt_766ec21deb5f929a37f2d02a940059f8=1668071801; OUTFOX_SEARCH_USER_ID_NCOO=764189497.8564049; ___rl__test__cookies=1668074757055; Hm_lpvt_766ec21deb5f929a37f2d02a940059f8=1668074886",
        "Host": "kjh.55128.cn",
        "Referer": "https://kjh.55128.cn/am6hc-history-300.htm",
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36"
    }

    try:
        r = requests.get(url, verify=False, headers=headers)
        r.encoding = 'utf-8'
        return r.text
    except Exception as e:
        print(e)
        return ""


# 获取所有的股票名称，将其放在一个列表中
def getStockList(stockURL):
    ll = []
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find('tbody').find_all('tr')
    spans = soup.find(class_='kaij-data').find(class_='kaij-cartoon').find_all('span')
    te = spans[7].string
    for i in a:
        try:
            num = i.find_all('td')[2].find_all('span')[7].string
            ll.append(int(num))
        except Exception as e:
            print(e)
            continue
    l = len(ll)
    ll.reverse()
    text = ''
    for k in range(0, l):
        # if int(te) == ll[k]:
        if 26 == ll[k]:
            lll = []
            for j in range(0, 7):
                if (k + j) < l:
                    lll.append(ll[k + j])
                    text = text + str(ll[k + j]) + ','
            text = text + '\n'
    print(text)
    # im = create_image(text)
    # im.show()
    # upload_file(im)


def create_image(text):
    im = Image.new("RGB", (200, 300), (255, 255, 255))
    dr = ImageDraw.Draw(im)
    # font = ImageFont.truetype(os.path.join("fonts", "msyh.ttf"), 14)
    dr.text((10, 5), text,  fill="#000000")
    # im.show()
    # im.save(r'D:\output.png')
    return im


def main():
    stock_list_url = 'https://kjh.55128.cn/am6hc-history-300.htm'
    getStockList(stock_list_url)


main()
