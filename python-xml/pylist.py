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

import xml.sax

class MovieHandler( xml.sax.ContentHandler ):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

        # Call when an element starts
        def startElement(self, tag, attributes):
            self.CurrentData = tag
            if tag == "movie":
                print ("*****Movie*****")
                title = attributes["title"]
                print ("Title:", title)

                # Call when an elements ends
                def endElement(self, tag):
                    if self.CurrentData == "type":
                        print ("Type:", self.type)
                    elif self.CurrentData == "format":
                        print ("Format:", self.format)
                    elif self.CurrentData == "year":
                        print ("Year:", self.year)
                    elif self.CurrentData == "stars":
                        print ("Stars:", self.stars)
                    elif self.CurrentData == "description":
                        print ("Description:", self.description)
                        self.CurrentData = ""

                        # Call when a character is readline
                        def characters(self, content):
                            if self.CurrentData == "type":
                                self.type = content
                            elif self.CurrentData == "format":
                                self.format = content
                            elif self.CurrentData == "year":
                                self.year = content
                            elif self.CurrentData == "rating":
                                self.rating = content
                            elif self.CurrentData == "stars":
                                self.rating = content
                            elif self.CurrentData == "description":
                                self.description = content

                                if (__name__ == "__main__"):

                                    # create an XMLReader
                                    parser = xml.sax.make_parser()
                                    # turn off namespaces
                                    parser.selfFeature(xml.sax.handler.feature_namespaces, 0)

                                    # override the default ContextHandler
                                    Handler = MovieHandler()
                                    parser.setContentHandler( Handler )

                                    parser.parse("list.xml")
