#!/usr/bin/env python3
# coding=utf-8
# Author: f43792
# License: MIT License
"""
    Scalable Vector Graphics (SVG) is an XML-based vector image format
    for two-dimensional graphics with support for interactivity and animation. 
    The SVG specification is an open standard developed by the World Wide Web 
    Consortium (W3C) since 1999.
    SVG images and their behaviors are defined in XML text files. 
    This means that they can be searched, indexed, scripted, and compressed. 
    As XML files, SVG images can be created and edited with any text editor, 
    as well as with drawing software. (From wikipedia)

    Simple functions handle units

Features:
    - Integrated units handling functions
    - Translation, rotation and scales capabilities
    - Easy real <-> scale translation
"""

version = (0, 0, 11)  # also update setup.py
VERSION = '{0}.{1}.{2}'.format(version[0], version[1], version[2])

AUTHOR_NAME = 'Fabio Cesar do Nascimento'
AUTHOR_EMAIL = 'f43792@gmail.com'
CYEAR = '2018-2020'
REPO = 'https://github.com/f43792/svgComposer.git'

# "1pt" equals "1.25px" (and therefore 1.25 user units)
# "1pc" equals "15px" (and therefore 15 user units)
# "1mm" would be "3.543307px" (3.543307 user units)
# "1cm" equals "35.43307px" (and therefore 35.43307 user units)
# "1in" equals "90px" (and therefore 90 user units)

MM = 3.543307
M = MM * 1000
CM = MM * 10
PT = 1.25
IN = 90

def mm(value):
    _mm = MM
    return value * _mm

def m(value):
    _m = MM
    return value * _m

def cm(value):
    _cm = CM
    return value * _cm

def pt(value):
    _pt = PT
    return value * _pt

def inches(value):
    _in = IN
    return value * _in