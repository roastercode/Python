#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Screen Scraping Parser
# Created on : Thu Nov 20 04:47:20 2014
#
# Write with Emacs-Nox
#
# References
#
# urlib urlopen HTMLParser
#
# Course material
#
# Python books - Own modification - Python Documentation - WWW
#
#


from urllib.request import urlopen
from html.parser import HTMLParser


class Scraper(HTMLParser):

    in_h3 = False
    in_link = False

    def handle_startag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h3':
            self.in_h3 = True

        if tag == 'a' and 'href' in attrs:
            self.in_link = True
            self.chuncks = []
            self.url = attrs['href']

    def handle_data(self, data):
        if self.in_link:
            self.chuncks.append(data)

    def handle_endtag(self, tag):
        if tag == 'h3':
            self.in_h3 = False
        if tag == 'a':
            if self.in_h3 and self.in_link:
                print ('%s (%s)') % (''.join(self.chuncks), self.url)
            self.in_link = False


text = urlopen('https://python.org/community/jobs').read()
parser = Scraper()
s = text
print (s)
