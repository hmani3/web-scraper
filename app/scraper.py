import requests
from bs4 import BeautifulSoup

def scraped_sites(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        jobs = []

    except Exception as e:
        return[f"Error: {e}"]

def job_title(soup):
    pass

