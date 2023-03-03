import math

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np


# 获取网页内容
def getHTMLText(url):
    headers = {
        "Cookie": "___rl__test__cookies=1668074718832; Hm_lvt_766ec21deb5f929a37f2d02a940059f8=1668071801; OUTFOX_SEARCH_USER_ID_NCOO=764189497.8564049; ___rl__test__cookies=1668074757055; Hm_lpvt_766ec21deb5f929a37f2d02a940059f8=1668074886",
        "Host": "kjh.55128.cn",
        "Referer": "https://kjh.55128.cn/hk6-history-2022.htm",
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
    for i in a:
        try:
            num = i.find('div','kaij-cartoon').find_all('span')[7].string
            ll.append(int(num))
        except Exception as e:
            print(e)
            continue

    # 导入数据
    x = list(np.arange(1, 61))
    # y = np.random.randn(20)
    ll.reverse()
    y=ll[-90:]
    x = list(np.arange(1, 91))
    # 设定画布。dpi越大图越清晰，绘图时间越久
    fig = plt.figure(figsize=(90, 50), dpi=200)
    # 绘图命令
    plt.plot(x, y, lw=2, ls='-', c='red', alpha=0.5)
    plt.scatter(x, y, c='red')
    # 汉字字体，优先使用楷体，找不到则使用黑体
    plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']

    # 正常显示负号
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("2022-", fontdict={'size': 20})
    for a, b in zip(x, y):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=24)
    # show出图形
    plt.show()
    # 保存图片
    fig.savefig("画布")



def main():
    stock_list_url = f'https://kjh.55128.cn/hk6-history-2022.htm'
    getStockList(stock_list_url)


main()
