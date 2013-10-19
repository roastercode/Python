#!/usr/bin python
# -*- coding: utf-8 -*-
# License   : GNU GPL v3 or later
# Author    : XL04D
# Mail      : aurelien@xload.IO
# Project   : Mail Emitter
# Find who emit the mail
# It the mail comes from a mailing list, it will give you
# the name of the emitter (which is not the sender)

import fileinput, re

pat = re.compile('From: (.*) <.*?>$')
for line in fileinput.input():
    m = pat.match(line)
    if m: print m.group(1)


# use the file mail to test the file
# 
# $ python mail_emitter.py mail
# Usul from Dune
