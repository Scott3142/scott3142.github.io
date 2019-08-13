import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

a, b = 10, 10
x = sym.symbols('x')
y = sym.exp(-x)
plot_beamer = sym.plot(y, (x,-a,a), show=False, xlim=[-a,a], ylim=[-b,b])
plot_beamer.save("../tex/beamer-pics/decreasing.pdf")

y = x**3
plot_beamer = sym.plot(y, (x,-a,a), show=False, xlim=[-a,a], ylim=[-b,b])
plot_beamer.save("../tex/beamer-pics/increasing.pdf")
