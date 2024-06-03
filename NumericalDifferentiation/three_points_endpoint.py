def three_point_forward_difference(f, x0, h):
    return (-3*f(x0) + 4*f(x0 + h) - f(x0 + 2*h)) / (2*h)

def three_point_backward_difference(f, xn, h):
    return (3*f(xn) - 4*f(xn - h) + f(xn - 2*h)) / (2*h)

def function(x):
    return x**3 + 10*x + 12

x0 = 0
xn = 2
h = 0.01

forward_diff = round(three_point_forward_difference(function, x0, h), 4)
backward_diff = round(three_point_backward_difference(function, xn, h), 4)

print(f"Three-Point Forward Difference at x0 = {x0}: {forward_diff}")
print(f"Three-Point Backward Difference at xn = {xn}: {backward_diff}")