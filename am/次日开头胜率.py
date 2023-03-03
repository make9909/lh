# coding:utf-8
import requests
from bs4 import BeautifulSoup

ll_his = [39, 16, 20, 45, 20, 32, 22, 17, 46, 44, 43, 14, 18, 25, 45, 48, 38, 8, 37, 11, 39, 1, 33, 46, 43, 25, 49, 18,
          7, 2, 37, 37, 32, 3, 39, 6, 35, 30, 44, 38, 9, 22, 7, 39, 43, 39, 34, 37, 23, 42, 17, 41, 45, 6, 25, 47, 19,
          5, 35, 11, 30, 34, 42, 25, 3, 36, 36, 40, 44, 37, 32, 41, 30, 37, 24, 39, 17, 15, 8, 9, 3, 14, 26, 46, 23, 48,
          5, 19, 34, 2, 33, 44, 6, 46, 33, 12, 16, 22, 46, 5, 40, 8, 10, 33, 1, 16, 28, 5, 47, 19, 2, 43, 1, 31, 44, 14,
          40, 24, 15, 19, 21, 28, 45, 38, 11, 26, 8, 22, 20, 13, 45, 5, 15, 47, 9, 15, 37, 4, 37, 17, 24, 20, 40, 4, 39,
          5, 26, 39, 49, 37, 10, 5, 28, 49, 12, 14, 7, 22, 48, 21, 36, 19, 29, 33, 47, 11, 14, 7, 28, 42, 43, 14, 43, 3,
          23, 2, 17, 18, 1, 20, 1, 26, 28, 47, 6, 10, 49, 30, 4, 6, 9, 41, 34, 9, 12, 45, 13, 14, 11, 28, 18, 2, 48, 36,
          25, 7, 27, 45, 3, 39, 31, 22, 37, 9, 36, 39, 11, 35, 8, 2, 46, 28, 48, 31, 42, 32, 49, 49, 33, 38, 31, 48, 3,
          7, 30, 38, 1, 42, 37, 23, 47, 45, 4, 1, 31, 35, 36, 27, 48, 22, 26, 45, 9, 23, 37, 14, 25, 34, 47, 8, 28, 46,
          39, 16, 14, 5, 7, 49, 14, 24, 13, 23, 23, 20, 12, 49, 8, 18, 15, 10, 10, 16, 5, 39, 41, 2, 20, 8, 21, 9, 26,
          23, 49, 3, 21, 27, 37, 10, 31, 16, 27, 30, 3, 40, 1, 32, 28, 31, 41, 8, 49, 39, 17, 31, 17, 33, 11, 24, 28,
          48, 21, 42, 14, 31, 47, 27, 11, 6, 33, 14, 21, 21, 42, 3, 37, 15, 49, 28, 1, 8, 17, 11, 29, 30, 33, 7, 8, 33,
          29, 35, 1, 3, 17, 37, 9, 2, 10, 8, 43, 45, 22, 2, 9, 41, 26]


# 获取网页内容
# 例如：今天开1头，明天开0 1 2 3 4 头的次数
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
    for i in a:
        try:
            num = i.find_all('td')[2].find_all('span')[7].string
            ll.append(int(num))
        except Exception as e:
            print(e)
            continue
    count0 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0

    count00 = 0
    count01 = 0
    count02 = 0
    count03 = 0
    count04 = 0

    count10 = 0
    count11 = 0
    count12 = 0
    count13 = 0
    count14 = 0

    count20 = 0
    count21 = 0
    count22 = 0
    count23 = 0
    count24 = 0

    count30 = 0
    count31 = 0
    count32 = 0
    count33 = 0
    count34 = 0

    count40 = 0
    count41 = 0
    count42 = 0
    count43 = 0
    count44 = 0
    ll.reverse()
    for j in range(0, len(ll) - 1):
        num = ll[j]
        if num < 10:
            count0 = count0 + 1
            num0 = ll[j + 1]
            if num0 < 10:
                count00 = count00 + 1
            if 10 <= num0 < 20:
                count01 = count01 + 1
            if 20 <= num0 < 30:
                count02 = count02 + 1
            if 30 <= num0 < 40:
                count03 = count03 + 1
            if 40 <= num0 < 50:
                count04 = count04 + 1
        if 10 <= num < 20:
            count1 = count1 + 1
            num1 = ll[j + 1]
            if num1 < 10:
                count10 = count10 + 1
            if 10 <= num1 < 20:
                count11 = count11 + 1
            if 20 <= num1 < 30:
                count12 = count12 + 1
            if 30 <= num1 < 40:
                count13 = count13 + 1
            if 40 <= num1 < 50:
                count14 = count14 + 1
        if 20 <= num < 30:
            count2 = count2 + 1
            num2 = ll[j + 1]
            if num2 < 10:
                count20 = count20 + 1
            if 10 <= num2 < 20:
                count21 = count21 + 1
            if 20 <= num2 < 30:
                count22 = count22 + 1
            if 30 <= num2 < 40:
                count23 = count23 + 1
            if 40 <= num2 < 50:
                count24 = count24 + 1
        if 30 <= num < 40:
            count3 = count3 + 1
            num3 = ll[j + 1]
            if num3 < 10:
                count30 = count30 + 1
            if 10 <= num3 < 20:
                count31 = count31 + 1
            if 20 <= num3 < 30:
                count32 = count32 + 1
            if 30 <= num3 < 40:
                count33 = count33 + 1
            if 40 <= num3 < 50:
                count34 = count34 + 1
        if 40 <= num < 50:
            count4 = count4 + 1
            num4 = ll[j + 1]
            if num4 < 10:
                count40 = count40 + 1
            if 10 <= num4 < 20:
                count41 = count41 + 1
            if 20 <= num4 < 30:
                count42 = count42 + 1
            if 30 <= num4 < 40:
                count43 = count43 + 1
            if 40 <= num4 < 50:
                count44 = count44 + 1
    print('0头:' + str(count0), '00:' + str(count00), '01:' + str(count01), '02:' + str(count02), '03:' + str(count03),
          '04:' + str(count04))
    print('1头:' + str(count1), '10:' + str(count10), '11:' + str(count11), '12:' + str(count12), '13:' + str(count13),
          '14:' + str(count14))
    print('2头:' + str(count2), '20:' + str(count20), '21:' + str(count21), '22:' + str(count22), '23:' + str(count23),
          '24:' + str(count24))
    print('3头:' + str(count3), '30:' + str(count30), '31:' + str(count31), '32:' + str(count32), '33:' + str(count33),
          '34:' + str(count34))
    print('4头:' + str(count4), '40:' + str(count40), '41:' + str(count41), '42:' + str(count42), '43:' + str(count43),
          '44:' + str(count44))


def main():
    stock_list_url = 'https://kjh.55128.cn/am6hc-history-300.htm'
    getStockList(stock_list_url)


main()
