import math

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np


# 获取网页内容
def getHTMLText(url):
    headers = {
        "Cookie": "Hm_lvt_5183b3347a186002cc935d712a90bade=1668241069,1668428296; Hm_lpvt_5183b3347a186002cc935d712a90bade=1668428311",
        "Host": "kjh.55128.cn",
        "Referer": "https://kjh.55128.cn/history_am6hc.aspx?selectyear=%E6%8C%89%E5%B9%B4%E4%BB%BD&newterm=2022217",
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
            spans = i.find_all('td')[2].find(class_='kaij-cartoon').find_all('span')
            num = spans[7].string
            ll.append(int(num))
        except Exception as e:
            print(e)
            continue

    # 导入数据
    x = list(np.arange(1, 31))
    # y = np.random.randn(20)
    ll.reverse()
    count = math.ceil(len(ll) / 30)
    for i in range(0, count):
        # 设定画布。dpi越大图越清晰，绘图时间越久
        fig = plt.figure(figsize=(30, 50), dpi=200)
        y = ll[i * 30:i * 30 + 30]
        if len(y) < 30:
            c = len(y) + 1
            x = list(np.arange(1, c))
            # 设定画布。dpi越大图越清晰，绘图时间越久
            fig = plt.figure(figsize=(len(y), 50), dpi=200)
            # 绘图命令
            plt.plot(x, y, lw=2, ls='-', c='red', alpha=0.5)
            plt.scatter(x, y, c='red')
            # 汉字字体，优先使用楷体，找不到则使用黑体
            plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']

            # 正常显示负号
            plt.rcParams['axes.unicode_minus'] = False
            plt.title("2022-" + str(i + 1), fontdict={'size': 20})
            for a, b in zip(x, y):
                plt.text(a, b, b, ha='center', va='bottom', fontsize=24)
            # show出图形
            plt.show()
            # 保存图片
            fig.savefig("画布" + str(i + 1))
        else:
            # 绘图命令
            plt.plot(x, y, lw=2, ls='-', c='red', alpha=0.5)
            plt.scatter(x, y, c='red')
            # 汉字字体，优先使用楷体，找不到则使用黑体
            plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']

            # 正常显示负号
            plt.rcParams['axes.unicode_minus'] = False
            plt.title("2022-" + str(i + 1), fontdict={'size': 20})
            for a, b in zip(x, y):
                plt.text(a, b, b, ha='center', va='bottom', fontsize=24)
            # show出图形
            plt.show()
            # 保存图片
            fig.savefig("画布" + str(i + 1))


def main():
    stock_list_url = f'https://kjh.55128.cn/am6hc-history-2022.htm'
    getStockList(stock_list_url)


main()
