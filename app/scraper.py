import requests, re
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',

}

def scraped(url):
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        names = get_names(soup)
        return names

    except Exception as e:
        print(f"response: {res.text}",flush=True)
        print(f"error: {e}",flush=True)
        return[f"Error: {e}"]

def get_names(soup):
    res = []
    ma1 = soup.find_all(class_="country-name")
    ma2 = soup.find_all(class_="country-capital")
    ma3 = soup.find_all(class_="country-population")
    ma4 = soup.find_all(class_="country-area")
    for i in range(len(ma1)): 
        res.append({"name": ma1[i].text, "capital": ma2[i].text, "population":ma3[i].text, "area":ma4[i].text})
    sort_res = sorted(res, key=lambda x: x["name"]) 
    return sort_res


