import requests
from glob import glob
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from time import sleep


# https://www.networkinghowtos.com/howto/common-user-agent-list/
HEADERS = ({'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
'Accept-Language': 'en-US, en;q=0.5'})

class Scraper:
    def __init__(self, urls):
        self.urls = urls
        
    def find_product(self):

# CSVファイルをインポートし、URLを取得
prod_tracker = pd.read_csv('trackers/TRACKER_PRODUCTS.csv', encoding='unicode-escape')
prod_tracker_URLS = prod_tracker.url

# URLをフェッチ
page = requests.get(prod_tracker_URLS[0], headers=HEADERS)



# URL内の全ての情報を含むオブジェクトを生成
soup = BeautifulSoup(page.content, 'lxml')

# 商品名
title = soup.find(id='productTitle').get_text().strip()


# 商品の価格が取得できなかった場合のクラッシュを防ぐ
try:
    price = float(soup.find(id='price').get_text().replace('¥', '').replace(',', '').strip())
except:
    # ドルで取得
    try:
        price = float(soup.find(id='newBuyBoxPrice').get_text().replace('$', '').replace(',', '').strip())
    except:
        print('Failed to get price')
        price = ''
print(price)