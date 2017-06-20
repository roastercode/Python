#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Python Experimentations
# Created on : June 2017
#
# Write with Emacs-Nox ──────────────┐
# Send Mail with attachment ─────────┘


import smtplib
import base64

filename = "/tmp/test"

# Read a file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
encodecontent = base64.b64encode(filecontent)  # base64

sender = 'from@hackers.camp'
receivers = 'to@tothedomain.com'

marker = "AUNIQUEMARKER"

body ="""
This is a test email to send an attachment.
"""

# Define the main headers.
part1 = """From: From Person <from@hackers.camp>
To: To Person <to@hackers.camp>
Subject: Sending Attachment
MIME-Version: 1.0
Content-Type: multipar/mixed; boundary=%s
--%s
""" % (marker, marker)

# Define the message action
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (body,marker)

# Define the attachement section
part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachement; filename=%s

%s
--%s--
""" %(filename, filename, encodecontent, marker)
message = part1 + part2 + part3

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, reciever, message)
    print ("Successfully sent email")
except Exception:
    print ("Error: unable to send email")
