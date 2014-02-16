#!/usr/bin python
# -*- coding: utf-8 -*-
# License   : GNU GPL v3 or later
# Author    : XL04D
# Mail      : aurelien@xload.IO
# Project   : somescript
# a bit of script

import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print 'Wordcount:', wordcount
