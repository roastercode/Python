#!/usr/bin/env python2
# -*- coding: utf-8 -*- 
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : factoriel - exercice 1
# Created on : Thu Nov 6 14:30:22 2014
#
# References
#
# python3 env
#
#
# Course material
#
# mooc python INRIA
#

def factoriel (n):
    "retourne le produit ...."
    if n <= 1:
        return 1
    else:
        return n * factoriel (n-1)
    
