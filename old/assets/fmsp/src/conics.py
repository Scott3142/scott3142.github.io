import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from sympy.plotting import plot_parametric

a, b = 10, 10
x = sym.symbols('x')
y = sym.sqrt(x)
p1 = sym.plot(y, (x,-a,a), show=False, xlim=[-a,a], ylim=[-b,b])
p2 = sym.plot(-y, (x,-a,a), show=False, xlim=[-a,a], ylim=[-b,b])
p1.extend(p2)
p1.save("../tex/beamer-pics/conics-parabola.pdf")

h,k = -0.5,0
a,b = 1,1
p1 = plot_parametric((h + a*sym.sec(x),k + b*sym.tan(x), (x,-1,1)),(-h - a*sym.sec(x),k + b*sym.tan(x), (x,-1,1)))
p1.save("../tex/beamer-pics/conics-hyperbola-1.pdf")

h,k = 0,0
a,b = 1,1
p1 = plot_parametric((h + a*sym.tan(x),k + b*sym.sec(x), (x,-1,1)),(h + a*sym.tan(x),-k - b*sym.sec(x), (x,-1,1)))
p1.save("../tex/beamer-pics/conics-hyperbola-2.pdf")

h,k = 0,0
a,b = 1,1
p1 = plot_parametric((h + a*sym.cos(x),k + b*sym.sin(x), (x,-2,2)),(-h - a*sym.cos(x),k + b*sym.sin(x), (x,-2,2)))
p1.save("../tex/beamer-pics/conics-ellipse.pdf")
