# coding:utf-8
import datetime
import io

import matplotlib.pyplot as plt
import numpy as np
import oss2
import pymysql
import requests
from PIL import Image
from bs4 import BeautifulSoup


Image.MAX_IMAGE_PIXELS = None
# ImageFile.LOAD_TRUNCATED_IMAGES = True


# 获取网页内容
def getHTMLText(url):
    headers = {
        "Cookie": "Hm_lvt_5183b3347a186002cc935d712a90bade=1668241069,1668428296; Hm_lpvt_5183b3347a186002cc935d712a90bade=1668428311",
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
    x = list(np.arange(1, 121))
    # y = np.random.randn(20)
    ll.reverse()
    y = ll[-120:]
    x = list(np.arange(1, 121))
    # 设定画布。dpi越大图越清晰，绘图时间越久
    fig = plt.figure(figsize=(90, 50), dpi=100)
    # 绘图命令
    plt.plot(x, y, lw=2, ls='-', c='red', alpha=0.5)
    plt.scatter(x, y, c='red')
    # 汉字字体，优先使用楷体，找不到则使用黑体
    plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']

    # 正常显示负号
    plt.rcParams['axes.unicode_minus'] = False
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    plt.title(current_date, fontdict={'size': 20})
    for a, b in zip(x, y):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=24)
    # show出图形
    plt.show()
    # 保存图片
    fig.savefig(current_date)
    # current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    # img_PIL = Image.open(current_date + '.png')
    # upload_file(img_PIL)


def upload_file(image):
    """
    上传文件
    :param oss_file_name: oss 上传文件名
    :param image: 图片文件
    :param local_file_path: 本地图片路径
    :return: oss文件访问路径
    """

    # oss 配置信息
    access_key_id = "LTAI4G53v12GTuTKLBdEXSkR"
    access_key_secret = "c73GzlKFguEnMORi3UzSxMuDO98oY8"
    bucket_name = "gzh-asset"
    region = "oss-cn-hangzhou"
    cdn_host = "http://gzh-asset.oss-cn-hangzhou.aliyuncs.com"

    # oss 授权
    auth = oss2.Auth(access_key_id, access_key_secret)
    # oss bucket
    endpoint = "https://" + region + ".aliyuncs.com"
    bucket = oss2.Bucket(auth, endpoint, bucket_name)
    # 将本地文件转为二进制流

    blob = image2byte(image)

    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    path = 'liuhe/line/' + current_date + '.png'
    # oss 开始上传
    bucket.put_object(path, blob)

    oss_url = cdn_host + '/' + path
    print('上传完成', oss_url)
    update_lh_info(oss_url, current_date)
    return oss_url


def image2byte(image):
    """
    图片转byte
    :param image: 必须是PIL格式
    :return: 二进制
    """
    # 创建一个字节流管道
    img_bytes = io.BytesIO()
    # 把PNG格式转换成的四通道转成RGB的三通道，然后再保存成jpg格式
    image = image.convert("RGB")
    # 将图片数据存入字节流管道， format可以按照具体文件的格式填写
    image.save(img_bytes, format="JPEG")
    # 从字节流管道中获取二进制
    image_bytes = img_bytes.getvalue()
    return image_bytes


def update_lh_info(gzh_lh, open_date):
    db = pymysql.connect(host='1.116.131.137', user='root', password='123456', port=8001, db='gzh_meida')
    cursor = db.cursor()
    sql = """update gzh_lh set line = '%s' WHERE open_date = '%s' """ % (gzh_lh, open_date)
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print('插入数据成功')
    except Exception as e:
        db.rollback()
        print("插入数据失败", e)
    db.close()


def main():
    stock_list_url = 'https://kjh.55128.cn/am6hc-history-120.htm'
    getStockList(stock_list_url)


main()
