import requests
from glob import glob
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from time import sleep
from selectorlib import Extractor


# https://www.networkinghowtos.com/howto/common-user-agent-list/
HEADERS = ({'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
'Accept-Language': 'en-US, en;q=0.5'})

# CSVファイルをインポートし、URLを取得
prod_tracker = pd.read_csv('trackers/TRACKER_PRODUCTS.csv', encoding='unicode-escape', sep='\t')
prod_tracker_URLS = prod_tracker.url

# URLをフェッチ
page = requests.get(prod_tracker_URLS[0], headers=HEADERS)

# URL内の全ての情報を含むオブジェクトを生成
soup = BeautifulSoup(page.content, 'lxml')

# 商品名
title = soup.find(id='productTitle').get_text().strip()
search_word = 'id=productTitle'
print(title)

extractor = Extractor.from_yaml_file('trackers/selectors.yml')
# 商品の価格が取得できなかった場合のクラッシュを防ぐ
# try:
price = soup.find(id='priceblock_ourprice').get_text().strip()
print(price)
# except:
#     print('Failed to get price')
#     price = ''
