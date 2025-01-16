import requests
from bs4 import BeautifulSoup

def scrape_news(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        ps = soup.find_all('a')
        return [p.get('href') for p in ps]
    except Exception as e:
        print(f"Error: {e}",flush=True)
        return[f"Error: {e}"]
