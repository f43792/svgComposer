from svgcomposer import Composer
from units import m, mm, inches

cps = Composer()

base = cps.add_svg_file('rsc/template.svg', 'base')
logo = cps.add_svg_file('rsc/svg-w3c-v.svg', 'logo')

logo.moveto(mm(40), inches(2))

cps.save('rsc/merged.svg')