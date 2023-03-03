import requests
from bs4 import BeautifulSoup


# 获取网页内容
def getHTMLText(url):
    headers = {
        "Cookie": "Hm_lvt_5183b3347a186002cc935d712a90bade=1668071800; OUTFOX_SEARCH_USER_ID_NCOO=764189497.8564049; ___rl__test__cookies=1668415281571; Hm_lpvt_5183b3347a186002cc935d712a90bade=1668415305",
        "Host": "kjh.55128.cn",
        "Referer": "https://kjh.55128.cn/am6hc-history-2021.htm",
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
    for k in range(1, 50):
        count = 0
        for j in range(0, len(ll)):
            if k == ll[j]:
                count = count + 1
        print(k, ':', count)
    print(ll)


def main():
    stock_list_url = 'https://kjh.55128.cn/am6hc-history-2021.htm'
    getStockList(stock_list_url)


main()
