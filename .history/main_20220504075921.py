import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from time import sleep

import Scraper
from get_api_token import get_api_token



def main():
    scraper = Scraper('trackers/TRACKER_PRODUCTS.csv')
    scraper.get_price()


   
    def send_line_notify(self, notification_message):
        """LINEに通知を送信する

        Args:
            notification_message (string): 通知メッセージ
        """
        line_notify_token = get_api_token()
        line_notify_api = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': f'Bearer {line_notify_token}'}
        data = {'message': f'message: {notification_message}'}
        requests.post(line_notify_api, headers = headers, data = data)

if __name__ == "__main__":
    main()
