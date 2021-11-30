import sympy
import matplotlib.pyplot as plt
import numpy


def build_graphic(x, y, new_x, expression):
    new_y = [expression.subs('x', i) for i in new_x]
    plt.plot(x, y, 'o', new_x, new_y)
    plt.show()


def lagrange(x, y, interpolation=False, x_in=None, graphic=False):
    expression = sympy.Add()
    for i in range(len(y)):
        local = sympy.Mul()
        for j in range(len(x)):
            if i != j:
                local *= sympy.sympify("(x - x_j)/(x_j - x_i)")
                local = local.subs([('x_i', x[i]), ('x_j', x[j])])
        expression += sympy.parse_expr('y_i') * local
        expression = expression.subs('y_i', y[i])
    ret = []
    if interpolation:
        ret.append(expression.subs('x', x_in))
    if graphic:
        build_graphic(x, y, numpy.linspace(numpy.min(x), numpy.max(x), 100), expression)

    ret.append(expression)
    return ret
