#!/usr/bin python
# -*- coding: utf-8 -*-
# License   : GNU GPL v3 or later
# Author    : XL04D
# Mail      : aurelien@xload.IO
# Project   : X search
# replace the X to search your wish

import fileinput, re
pat = re.compile(r'[a-z\-\.]+X[a-z\-\.]+', re.IGNORECASE)
files = set()
for line in fileinput.input():
    for X in pat.findall(line):
        files.add(X)
    for X in sorted(files):
        print X
        

# replace X between ]+X[ by the word you wish
# $ python x_search.py <file>
