#!/usr/bin/env python
# -*- coding : utf-8 -*-

from bs4 import BeautifulSoup

html_file = open("tmp.html", "r")
html_doc = html_file.read()
html_file.close()
soup = BeautifulSoup(html_doc)

table = soup.findAll('table')[10]
cols = table.findAll('td')
for date in table.findAll('td', attrs={'class' : 'header_date'}):
    data = date.findAllNext('td', attrs={'class' : 'forum_thread_post'}, limit = 3)
    print date.findAll('b')
    print data[2]
