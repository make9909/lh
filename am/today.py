# coding:utf-8

import requests
from bs4 import BeautifulSoup


# 获取网页内容
def getHTMLText(url):
    headers = {
        "Cookie": "___rl__test__cookies=1668074718832; Hm_lvt_766ec21deb5f929a37f2d02a940059f8=1668071801; OUTFOX_SEARCH_USER_ID_NCOO=764189497.8564049; ___rl__test__cookies=1668074757055; Hm_lpvt_766ec21deb5f929a37f2d02a940059f8=1668074886",
        "Host": "kjh.55128.cn",
        "Referer": "https://kjh.55128.cn/am6hc-history-120.htm",
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
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    spans = soup.find(class_='kaij-cartoon').find_all('span')
    ping_code = spans[0].string + ',' + spans[1].string + ',' + spans[2].string + ',' + spans[3].string + ',' + spans[
        4].string + ',' + spans[5].string
    special_code = spans[7].string
    print(ping_code, special_code)


def main():
    stock_list_url = 'https://kjh.55128.cn/am6hc-history-120.htm'
    getStockList(stock_list_url)


main()
