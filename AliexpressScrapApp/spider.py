import requests
from bs4 import BeautifulSoup

def spider(url):
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    r = requests.get(url, headers = header, timeout = 30)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup