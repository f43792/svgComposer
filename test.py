from svgcomposer import Composer
from units import m, mm

cps = Composer()

t = cps.add_svg_file('rsc/template.svg', 'tem')
r = cps.add_svg_file('rsc/rect.svg', 'rec')

r.moveto(mm(40), 0)

cps.save('rsc/merged.svg')