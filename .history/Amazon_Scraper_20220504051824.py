import requests
from glob import glob
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from time import sleep
from selectorlib import Extractor
import json
import html


# https://www.networkinghowtos.com/howto/common-user-agent-list/
# HEADERS = ({'User-Agent':
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
# 'Accept-Language': 'en-US, en;q=0.5'})

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

# CSVファイルをインポートし、URLを取得
prod_tracker = pd.read_csv('trackers/TRACKER_PRODUCTS.csv', encoding='unicode-escape', sep='\t')
prod_tracker_URLS = prod_tracker.url

# 抽出したい要素をyamlファイルから読み込む
extractor = Extractor.from_yaml_file('trackers/selectors.yml')
# print(extractor.extract())

# URLをフェッチ
page = requests.get(prod_tracker_URLS[0], headers=HEADERS)



# URL内の全ての情報を含むオブジェクトを生成
soup = BeautifulSoup(page.content, 'lxml')

# 商品名
title = soup.find(id='productTitle').get_text().strip()

# to prevent script from crashing when there isn't a price for the product
try:
    price = float(soup.find(id='priceblock_ourprice').get_text().replace('.', '').replace('€', '').replace(',', '.').strip())
except:
    # this part gets the price in dollars from amazon.com store
    try:
        price = float(soup.find(id='priceblock_saleprice').get_text().replace('$', '').replace(',', '').strip())
    except:
        print('fail')
        price = ''
# 商品の価格が取得できなかった場合のクラッシュを防ぐ
# try:
# price = soup.find(id='priceblock_ourprice').get_text().strip()
# print(page.content)
# print(price)
# except:
#     print('Failed to get price')
#     price = ''
