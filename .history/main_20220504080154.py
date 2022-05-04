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


   
if __name__ == "__main__":
    main()
