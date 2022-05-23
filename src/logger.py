import pandas as pd
from datetime import datetime


class Logger:
    """ログに関連する関数を集めたクラスです
    """
    def __init__(self):
        self.tracker_log = pd.DataFrame()
        self.now = datetime.now().strftime('%Y-%m-%d %H%Mm')

    def create_log(self, name, url, title, buy_below, price):
        """ログを生成します

        Args:
            name (str): csvファイル内の名前
            url (str): 商品URL
            title (str): 商品名
            buy_below (float): 購入したい価格
            price (float): 実際の価格

        Returns:
            _type_: _description_
        """
        log = pd.DataFrame({'date': self.now.replace('h', ':').replace('m', ''),
        'name': name,
        'url': url,
        'title': title,
        'buy_below': buy_below,
        'price': price})
        return log

    def save_log(self, name, url, title, buy_below, price):
        """ログを保存します

        Args:
            name (str): csvファイル内の名前
            url (str): 商品URL
            title (str): 商品名
            buy_below (float): 購入したい価格
            price (float): 実際の価格
        """
        log = self.create_log(name, url, title, buy_below, price)
        self.tracker_log = pd.concat([self.tracker_log ,log])
        print('+++++++++++++++++++++++++++++++++')
        print(self.tracker_log)
        print('+++++++++++++++++++++++++++++++++')