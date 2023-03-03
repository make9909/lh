import requests
from bs4 import BeautifulSoup


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
    ll = ''
    count0 = 0
    count1 = 0
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find('tbody').find_all('tr')
    for i in a:
        try:
            num = i.find('div','kaij-cartoon').find_all('span')[7].string
            if int(num) % 2 == 0:
                ll = ll + '0'
                count0 = count0 + 1
            else:
                ll = ll + '1'
                count1 = count1 + 1
        except Exception as e:
            print(e)
            continue
    # for k in range(1, 50):
    #     count = 0
    #     for j in range(0, 304):
    #         if k == ll[j]:
    #             count = count + 1
    #     print(k, ':', count)
    print(ll)
    print('count0:', count0, 'count1:', count1)


def main():
    stock_list_url = f'https://kjh.55128.cn/hk6-history-2022.htm'
    getStockList(stock_list_url)


main()
