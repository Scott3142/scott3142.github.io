import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def save_tex_questions(y,num):
    with open("../tex/examples/questions/graph-sketch-" + str(num) + ".tex", "w") as f:
        f.write(sym.latex(y))

def save_plots_examples(x,y,a,b,num):
    plot_solutions = sym.plot(y, (x,-a,a), show=False, xlim=[-a,a], ylim=[-b,b])
    plot_solutions.save("../tex/examples/solutions/graph-sketch-solutions-" + str(num) + ".pdf")

    if num == 1:
        plot_empty = sym.plot(y, (x,-a,a), show=False, xlim=[-a,a], ylim=[-b,b], line_color='white')
        plot_empty.line_color = 'w'
        plot_empty.save("../tex/examples/questions/graph-sketch-questions.pdf")

def save_plots_beamer(x,y,a,b,num):
    plot_beamer = sym.plot(y, (x,-a,a), show=False, xlim=[-a,a], ylim=[-b,b])

    if num <= 5:
        plot_beamer.save("../tex/beamer-pics/asymptote-" + str(num) + ".pdf")
    elif num == 6:
        plot_beamer.save("../tex/beamer-pics/even.pdf")
    elif num == 7:
        plot_beamer.save("../tex/beamer-pics/odd.pdf")
    elif num == 8:
        plot_beamer.save("../tex/beamer-pics/image.pdf")

a, b = 10, 10
x = sym.symbols('x')
y = [1/x, x/(x-1)**2, (x+1)**2/((x-1)*(x-2)), (x**2+4)/x, (1+x)/(1-x), (x-1)/(1+x), (x+1)*(x+2)/((x-1)*(x-2)), 1/((x)*(x**2 + 1)), (x**2 + 2*x + 1)*(x-1)/((x+1**2)), sym.sin(1/x)]

for i in range(len(y)):
    save_tex_questions(y[i],i+1)
    save_plots_examples(x,y[i],a,b,i+1)

y = [(x+1)**2/((x-1)*(x-2)), (5-3*x)/(x-3), (x**2+4)/x, x*(x+3)/(x-1),x**3+2*x**2+x,sym.cos(x),sym.sin(x),x**2+x+1]

for i in range(len(y)):
    if i <= 4:
        save_plots_beamer(x,y[i],a,b,i+1)
    elif i <= 6:
        save_plots_beamer(x,y[i],a,b-8.5,i+1)
    elif i == 7:
        save_plots_beamer(x,y[i],5,10,i+1)
