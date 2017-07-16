# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 07:45:24 2017

@author: SiddheshPisal
"""

import urllib2 # module to read in HTML
import bs4 # BeautifulSoup: module to parse HTML and XML
import json # 
import datetime as dt # module for manipulating dates and times
import pandas as pd
import numpy as np

x = urllib2.urlopen("http://www.google.com")
htmlSource = x.read()
x.close()

type(htmlSource)
print htmlSource

x = urllib2.urlopen("http://www.reddit.com") # Opens URLS
htmlSource = x.read()
x.close()
print htmlSource

soup = bs4.BeautifulSoup(htmlSource)
print soup.prettify()

print soup.head.prettify()

soup.head.contents
len(soup.head.contents)
soup.head.contents[0:3]
soup.head.children

for child in soup.head.children:
    print child
    print ""
    
soup.head.title
soup.head.title.string

for child in soup.head.descendants:
    print child
    print ""
    
for string in soup.strings:
    print(repr(string))
    print ""
    
for string in soup.stripped_strings:
    print(repr(string))
    
soup.title
soup.title.string
soup.title.string.parent

soup.find_all('a')
soup.find_all('p')
soup.find_all('table')

soup.find_all('a', limit = 10)

soup.find_all('a')[1].get('href')

for link in soup.find_all('a'):
    print(link.get('href'))
    

for link in soup.find_all('a', limit = 6):
    print(link.get('href'))

print soup.get_text()

a = {'a': 1, 'b':2}
s = json.dumps(a)
a2 = json.loads(s)

url = "http://worldcup.sfg.io/matches"
data = urllib2.urlopen(url).read()
wc = json.loads(data.decode('utf-8'))

"Number of matches in 2014 World Cup: %i" % len(wc)
gameIndex = 42
wc[gameIndex].keys()
wc[gameIndex]['status']
wc[gameIndex]['match_number']
wc[gameIndex]['away_team']
wc[gameIndex]['away_team_events']
wc[gameIndex]['home_team']

for elem in wc:
    print elem['home_team']['country'],elem['home_team']['goals'], elem['away_team']['country'],elem['away_team']['goals']
   
data = pd.DataFrame(wc, columns = ['match_number', 'location', 'datetime', 'home_team', 'away_team', 'winner', 'home_team_events', 'away_team_events'])
data.head()

data['gameDate'] = pd.DatetimeIndex(data.datetime).date
data['gameTime'] = pd.DatetimeIndex(data.datetime).time
data.head()

