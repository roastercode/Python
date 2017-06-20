#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Python Box
# Created on : Mon Jun 19 14:13 2017
#
# Write with Emacs-Nox ──────────────┐
# Python3 Send Mail ─────────────────┘


import smtplib
import string

"""This script
send mail"""

sender = 'from@hackers.camp'
receivers = ['to@tothedomain.com']

message = """From: From Person <from@hackers.camp>
To: To Person <to@tothedomain.com>
Subject: SMTP e-mail message.
"""

try:
    smtpObj = smtp.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print("Successfully sent email")
except SMTPException:
    print("Error: unable to send email")
    mail = smtplib.SMTP('smtp.gmail.com', 587)
