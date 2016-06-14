#! /usr/bin/python3
# weatherScraper.py
import bs4
import urllib
import re
import textMyself

r = urllib.request.urlopen('http://forecast.weather.gov/MapClick.php?lat=43.665008355852024&lon=-70.30798472131704#.V18VRx9vEXc')
soup = bs4.BeautifulSoup(r, 'html5lib')



weather = soup.select('#detailed-forecast-body > .row.row-odd.row-forecast > .col-sm-10.forecast-text')
todayWeather = weather[0].getText()

precipRegex = re.compile(r'Chance of precipitation is \d\d%')
try:
    precipChance = precipRegex.search(todayWeather).group()
    if precipChance:
        textMyself.textmyself(precipChance)
    else:
        textMyself.textmyself('No rain today')
except:
    textMyself.textmyself('No rain today')
