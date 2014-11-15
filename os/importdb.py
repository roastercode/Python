#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Import DB
# Created on : Sat Nov 15 16:52:47 2014
#
# Write with Emacs-Nox
#
# References
#
# import sqlite3 def
#
# Course material
#
# Python book
#

# In a folder
# run that file with a db_file (plain text) from terminal
#
# python importdb.py "desktop <= 100 AND wm >= 50 ORDER BY os"
#
# that will create a new file name os_sys.db
#

import sqlite3

def convert(value):
    if value.startswith('~'):
        return value.strip('~')
        if not value:
            value = '0'
        return float(value)


conn = sqlite3.connect('os_sys.db')
curs = conn.cursor()

curs.execute('''
CREATE TABLE faif (
  id           TEXT       PRIMARY KEY,
  os           TEXT,
  desktop      FLOAT,
  wm           FL0AT,
  editor       FL0AT

)
''')


query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'

for line in open('db_file'):
    fields = line.split('^')
    vals = [convert(f) for f in fields[:field_count]]
    curs.execute(query, vals)

conn.commit()
conn.close()
