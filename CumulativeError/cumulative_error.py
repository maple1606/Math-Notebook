import numpy as np

def f(x, y):
    return x**2 * np.sin(y) + y**3 * np.cos(x)

def diff(f, x, h):
    return (f(x+h) - f(x-h)) / (2*h)

def partial_diff(f, x, idx, h):
    x_plus = list(x)
    x_minus = list(x)
    x_plus[idx] += h
    x_minus[idx] -= h
    return (f(*x_plus) - f(*x_minus)) / (2*h)

def direct_solver(f, x, x_abs_err, h):
    if type(x) is float:
        x = [x]
        x_abs_err = [x_abs_err] 
    res = 0
    for i in range(len(x)):
        res += abs(partial_diff(f, x, i, h)) * x_abs_err[i]
    return res

def inverse_solver(f, x, y_abs_err, h):
    if isinstance(x, float):
        return y_abs_err / abs(diff(f, x, h))
    res = []
    for i in range(len(x)):
        res.append(round(y_abs_err / abs(partial_diff(f, x, i, h)), 4))
    return res

x_point = [1.0, 0.5]
tolerance = 0.01

x_error = [0.01, 0.01]
print("Cumulative output error:", round(direct_solver(f, x_point, x_error, tolerance), 4))

y_abs_err = 0.05
print("Maximum estimated input errors:", inverse_solver(f, x_point, y_abs_err, tolerance))