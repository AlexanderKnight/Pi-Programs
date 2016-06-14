import bs4
import requests
import urllib

r = urllib.request.urlopen('https://weather.com/weather/today/l/USME0328:1:US').read()
#res = requests.get('https://weather.com/weather/today/l/USME0328:1:US')
#res.raise_for_status()
soup = bs4.BeautifulSoup(r, 'html5lib')
print(soup)
precipChance = soup.find_all("span", class_="precip-val")
#weatherSoup = bs4.BeautifulSoup(res.text, "html.parser")
#precipChance = weatherSoup.find_all("span", class_="precip-val")
print(precipChance)
