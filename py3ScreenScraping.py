#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Screen Scraping
# Created on : Wed Nov 19 21:14:03 2014
#
# Write with Emacs-Nox
#
# References
#
# urllib urlopen decode
#
# Course material
#
# Python books - Own modification - Python Documentation - WWW
#
#

from urllib.request import urlopen
import re

p = re.compile('<h3><a .*?><a .*? href="(.*?)">(.*?)</a>')
text = urlopen('http://www.hackers-lab.org').read()
for url, name in p.findall(text.decode()):
     print ('%s)') % (name, url)
