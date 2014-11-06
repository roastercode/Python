#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Fibonnacci
# Created on : Thu Nov 6 17:47:39 2014
#
#
# Course material
#
# MOOC INRIA PYTHON
#
# 

from argparse import ArgumentParser

def fibonacci (n):
    "retourne le nombre de fibonacci pour l'entier n"
    if n <= 1 : 
        return 1
    f2, f1 = 1, 1
    for i in range (2,n+1):
        f2, f1 = f1, f1+f2
#        print i, f2, f1
    return f1

parser = ArgumentParser ()
parser.add_argument (dest="entier", type=int, 
                     help="entier d'entree")
input_args = parser.parse_args()
entier = input_args.entier
print "fibonacci({}) = {}".format(entier, fibonacci (entier))

