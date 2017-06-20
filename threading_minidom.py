#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Python Experimentations
# Created on : June 2017
#
# Write with Emacs-Nox ──────────────┐
# Python3 XML ───────────────────────┘

from  xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root element : %s" % collection.getAttribute("shelf"))

    # Get all the movies in the collections
    movies = collection.getElementByTagName("movie")

    # Print detail of each movie.
    for movie in movies:
        print("*****Movie*****")
        if movie.hasAttribute("title"):
            print("Title: %s" % movie.getAttribute("title"))

            type = movie.getElementByTagName('type')[0]
            print("Type: %s" % type.childNodes[0].data)
            format = movie.getElementByTagName('format')[0]
            print("Format: %s" % format.childNodes[0].data)
            rating = movie.getElementByTagName('rating')[0]
            print("Rating: %s" % rating.childNodes[0].data)
            description = movie.getElementByTagName('description')[0]
            print("Description: %s" % description.childNodes[0].data)
            
