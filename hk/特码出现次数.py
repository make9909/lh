import requests
from bs4 import BeautifulSoup


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
    l1 = []
    for i in a:
        try:
            spans = i.find_all('td')[2].find(class_='kaij-cartoon').find_all('span')
            num = spans[7].string
            ll.append(int(num))
        except Exception as e:
            print(e)
            continue
    for k in range(1, 50):
        count = 0
        for j in range(0, len(ll)):
            if k == ll[j]:
                count = count + 1
        d1 = {'num': k, 'value': count}
        l1.append(d1)
        # print(k, ':', count)
    l1_ = sorted(l1, key=lambda x: x['value'], reverse=True)
    print(l1_)

    for l in l1_:
        r = l['value'] / len(ll) * 100
        print(l['num'], ':', l['value'], ':', '{:.3f}%'.format(r))


def main():
    stock_list_url = f'https://kjh.55128.cn/am6hc-history-2022.htm'
    getStockList(stock_list_url)


main()
