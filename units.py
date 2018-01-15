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

MM = 3.543307
M = MM * 1000

def mm(value):
    _mm = MM
    return value * _mm

def m(value):
    _m = MM
    return value * _m