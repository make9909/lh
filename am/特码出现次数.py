# coding:utf-8
import datetime
import io
import os
import oss2
import pymysql

import requests
from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup


# 获取网页内容
# 采集特码近一年出现次数
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
    l1 = []
    for i in a:
        try:
            num = i.find_all('td')[2].find_all('span')[7].string
            ll.append(int(num))
        except Exception as e:
            print(e)
            continue
    for k in range(1, 50):
        count = 0
        for j in range(0, len(ll)):
            if k == ll[j]:
                count = count + 1
        if k < 10:
            if count < 10:
                d1 = {'num': '0' + str(k), 'value': '0' + str(count)}
            else:
                d1 = {'num': '0' + str(k), 'value': str(count)}
        else:
            if count < 10:
                d1 = {'num': str(k), 'value': '0' + str(count)}
            else:
                d1 = {'num': str(k), 'value': str(count)}
        l1.append(d1)
        # print(k, ':', count)
    l1_ = sorted(l1, key=lambda x: x['value'], reverse=True)
    print(l1_)

    text = ''
    count = 0
    for l in l1_:
        count = count + 1
        if count % 7 == 0:
            text = text + (l['num']) + ':' + (l['value']) + '     \n'
        else:
            text = text + (l['num']) + ':' + (l['value']) + '     '
    print(text)


def main():
    stock_list_url = 'https://kjh.55128.cn/am6hc-history-300.htm'
    getStockList(stock_list_url)


main()
