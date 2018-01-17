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

version = (0, 0, 2)  # also update setup.py
VERSION = '{0}.{1}.{2}'.format(version[0], version[1], version[2])

AUTHOR_NAME = 'Fabio Cesar do Nascimento'
AUTHOR_EMAIL = 'f43792@gmail.com'
CYEAR = '2018-2020'
REPO = 'https://github.com/f43792/svgComposer.git'

# SCALE = 1.0 # Scale of real size object to svg

# def mm(value):
#     _mm = _MM
#     return value * _mm * SCALE

# def m(value):
#     _m = _M
#     return value * _m * SCALE

# def cm(value):
#     _cm = _CM
#     return value * _cm * SCALE

# def pt(value):
#     _pt = _PT
#     return value * _pt * SCALE

# def inches(value):
#     _in = _IN
#     return value * _in * SCALE

# def px(value):
#     _px = _PX
#     return value * _px

class Unit(object):
    """ Class to handle unit convertions. Result is always in pixels (px)  """
    _IN = 96 # Inkscape 0.92 changed to 96 pixel per Inche (was 90/in)
    _MM = _IN / 25.4 #3.7795275590551181102362204724409
    _M = _MM * 1000
    _CM = _MM * 10
    _PT = 1.33333333333333
    _PX = 1

    _RATIOS = { 'in': _IN,
                'mm': _MM,
                'm' : _M,
                'cm': _CM,
                'pt': _PT,
                'px': _PX
                }

    def __init__(self, unitStr='mm', scale=1.0):
        self._scale = scale
        unitStr = unitStr.lower()
        try:
            self._ratio = self._RATIOS[unitStr]
        except:
            print('Unknow lenght unit.')
            raise

    def __rmul__(self, value):
        """ Return the value multiplied by ratio __ """
        return value * self._ratio * self._scale

    def __call__(self, values):
        """ When called, multiply the arguments by ratio """
        if (type(values) == tuple or type(values) == list):
            res = []
            for v in values:
                res.append(v * self._ratio * self._scale)
            if type(values) == tuple:
                res = tuple(res)
            return res
        else:
            return values * self._ratio * self._scale

mm = Unit('mm')
m = Unit('m')
cm = Unit('cm')
inches = Unit('in')
pt = Unit('pt')
px = Unit('px')