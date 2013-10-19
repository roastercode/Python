#!/usr/bin python
# -*- coding: utf-8 -*-
# License   : GNU GPL v3 or later
# Author    : XL04D
# Mail      : aurelien@xload.IO
# Project   : Mail Sender
# Find who send a mail
# if it comes from a mailing list, you will know which one

import fileinput, re

pat = re.compile('Sender: (.*) <.*?>$')
for line in fileinput.input():
    m = pat.match(line)
    if m: print m.group(1)

# use the file mail to test the file
# 
# $ python mail_send.py mail
# "gigantic-worms"
