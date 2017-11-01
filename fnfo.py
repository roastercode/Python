#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Python Box
# Created on : Thu Nov 13 12:01:03 2014
# Modified   : Wed Nov 1 2017
# Write with Emacs-Nox
#
# Pylint verified 10.00
#
""" Python experimentations """

import math
import datetime

# print documentation about print
help(print)

# Print the explanation
print('This place is made for experimentations!')

# print documentation about math
help(math)
dir(math)

# print documentation about math
help(math.radians)
math.radians(180)
print(math.radians)

# information about datetime
dir(datetime)

# documenation about datetime
help(datetime)

# print the date
AD = datetime.date(1975, 5, 24)
print(AD.strftime("Aurélien was born: %A, %B %d, %Y"))

# another printing formatted way
MESSAGE = "Aurélien was born on {:%A, %B %d, %Y}."
print(MESSAGE.format(AD))

# date & time
LAUNCH_DATE = datetime.date(2017, 11, 1)
LAUNCH_TIME = datetime.time(10, 00, 0)
LAUNCH_DATETIME = datetime.datetime(2017, 11, 1, 10, 00, 0)
print(LAUNCH_TIME)
print(LAUNCH_DATE)
print(LAUNCH_DATETIME)
