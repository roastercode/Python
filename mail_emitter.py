#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : mail emitter
# Created on : 
#
# References
#
# python3 env
#
#
# Course material
#
#

import fileinput, re

pat = re.compile('From: (.*) <.*?>$')
for line in fileinput.input():
    m = pat.match(line)
    if m: print m.group(1)


# use the file mail to test the file
# 
# $ python mail_emitter.py mail
# Usul from Dune
