# -*- coding: utf-8 -*-
"""
Created on Sat May 14 10:52:14 2016

@author: silver
"""

#! python3
# lucky.py - Opens several Google search results
import requests, sys, webbrowser, bs4

print('Googling...') # Display text while downloading the page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)


linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com'+linkElems[i].get('href'))