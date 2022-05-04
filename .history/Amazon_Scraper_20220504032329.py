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

# CSVファイルをインポートし、URLを取得
prod_tracker = pd.read_csv('trackers/TRACKER_PRODUCTS.csv', encoding='unicode-escape')
print(prod_tracker.columns)
# prod_tracker_URLS = prod_tracker.url
# print(prod_tracker_URLS)

# URLをフェッチ
# page = requests.get(prod_tracker_URLS[0], header=HEADERS)

# URL内の全ての情報を含むオブジェクトを生成
# soup = BeautifulSoup(page.content, features='lxml')

