import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

a, b = 10, 10
x = sym.symbols('x')
y = (x+1)/(x-1)
plot_beamer = sym.plot(y, (x,-a,a), show=False, xlim=[-a,a], ylim=[-b,b])
plot_beamer.save("../tex/beamer-pics/continuous-1.pdf")

y1 = x**2 - 2x + 4
y2 = - x**2 + 6x - 7
plot_beamer = sym.plot(y1, (x,0,2), show=False, xlim=[0,4], ylim=[-b,b])
plot_beamer = sym.plot(y2, (x,2,4), show=False, xlim=[0,4], ylim=[-b,b])
plot_beamer.save("../tex/beamer-pics/continuous-2.pdf")
