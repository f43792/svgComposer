from svgcomposer import Composer
from units import m, mm, inches
import os
import sys

# Import unit path to sys path
looking_path = os.path.join(os.path.dirname(__file__), 'rsc')
cps = Composer()

base = cps.add_svg_file(os.path.join(looking_path, 'template.svg'),  'base')
logo = cps.add_svg_file(os.path.join(looking_path, 'svg-w3c-v.svg'), 'logo')

if base and logo:
    logo.moveto(mm(150), inches(2))

cps.save(os.path.join(looking_path, 'merged.svg'))