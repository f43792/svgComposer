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

    Simple class to easily handle and merge diferent svg files

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

from os.path import exists as fileExists

try:
    import svgutils.transform as st
except ImportError:
    print('Module svgutils not found. \nInstall it by using "pip3 install svgutils".')

class Composer(object):
    """
    Main SVG compositor class.
    """
    def __init__(self, width=None, height=None):
        """
        Compositor creator function
        """
        # Main SVG initialization
        self.__mainSVG = None
        if ((height != None) and (width != None)):
            self.__mainSVG = st.SVGFigure(width, height)
        else:
            self.__mainSVG = st.SVGFigure()
        self.__SVGS = {}

    def add_svg_file(self, svgfile, objname):
        """
        Add a svg file to the composition
        """
        if fileExists(svgfile):
            root = st.fromfile(svgfile).getroot()
            self.__SVGS[objname] = root
            return self.__SVGS[objname]
        else:
            print('File {fl} not found.'.format(fl=svgfile))

    def save(self, filename):
        """ 
        Save composited SVG
        """
        objects = []
        for obj in self.__SVGS:
            objects.append(self.__SVGS[obj])
        nobjs = len(objects)
        if nobjs > 0:
            self.__mainSVG.append(objects)
            self.__mainSVG.save(filename)
        else:
            print('No objects to save.')
