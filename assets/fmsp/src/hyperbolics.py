import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def save_plots_beamer(x,y,a,b,num):
    plot_beamer = sym.plot(y, (x,-a,a), show=False, xlim=[-a,a], ylim=[-b,b])
    plot_beamer.save("../tex/beamer-pics/hyperbolics-" + str(num) + ".pdf")

a, b = 10, 10
x = sym.symbols('x')
y = [sym.sinh(x),sym.cosh(x),sym.tanh(x),sym.asinh(x),sym.acosh(x),sym.atanh(x)]

for i in range(len(y)):
    save_plots_beamer(x,y[i],a,b,i+1)
