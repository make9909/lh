import re

import requests
from bs4 import BeautifulSoup


# 获取网页内容
def getHTMLText(url):
    headers = {
        "Cookie": "___rl__test__cookies=1668074718832; Hm_lvt_766ec21deb5f929a37f2d02a940059f8=1668071801; OUTFOX_SEARCH_USER_ID_NCOO=764189497.8564049; ___rl__test__cookies=1668074757055; Hm_lpvt_766ec21deb5f929a37f2d02a940059f8=1668074886",
        "Host": "m.55128.cn",
        "Referer": "http://m.55128.cn/zs/225_4418.htm",
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
            num = i.find_all('td')[1].span.string
            ll.append(int(num))
        except Exception as e:
            print(e)
            continue
    l = len(ll)
    for k in range(0, l):
        if 6 == ll[k]:
            lll = []
            for j in range(0, 7):
                if (k + j) < l:
                    lll.append(ll[k + j])
            print(lll)


def main():
    stock_list_url = f'http://m.55128.cn/zs/225_4414.htm'
    getStockList(stock_list_url)


main()
