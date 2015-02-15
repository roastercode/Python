#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Beautiful Soup Screen Scraper
# Created on : Sat Nov 22 07:59:04 2014
#
# Write with Emacs-Nox
#
# References
#
# Beautiful Soup urlib urlopen bs4
#
# Course material
#
# Python books - Own modification - Python Documentation - WWW
# 


from urllib.request import urlopen
from bs4 import BeautifulSoup

text = urlopen('https://python.org/community/jobs').read()
soup = BeautifulSoup(text)

jobs = set()
for header in soup('h1'):
    links = header('a', 'reference')
    if not links:
        continue
    link = links[0]
    jobs.add('%s (%s)' % (link.string, link['href']))

print('\n'.join(sorted(jobs, key=lambda s: s.lower())))
