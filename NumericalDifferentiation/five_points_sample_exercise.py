data = {
    1.05: -1.709847, 
    1.10: -1.373823, 
    1.15: -1.119214, 
    1.20: -0.9160143,
    1.25: -0.7470223, 
    1.30: -0.6015966}

def f(x):
    return data[round(x, 2)]

def five_point_forward_difference(f, x0, h):
    return (-25*f(x0) + 48*f(x0+h) - 36*f(x0+2*h) + 16*f(x0+3*h) - 3*f(x0+4*h)) / (12*h)

def five_point_backward_difference(f, x, h):
    return (25*f(xn) - 48*f(xn-h) + 36*f(xn-2*h) - 16*f(xn-3*h) + 3*f(xn-4*h)) / (12*h)

def five_point_central_difference(f, x, h):
    return (f(x-2*h) - 8*f(x-h) + 8*f(x+h) - f(x+2*h)) / (12*h)

h = 0.05
x0 = 1.05
xn = 1.30
x_values = [1.05, 1.10, 1.15, 1.20, 1.25, 1.30]

f_prime = []

f_prime.append(round(five_point_forward_difference(f, x0, h), 4))
f_prime.append(round(five_point_forward_difference(f, x0+h, h), 4))

for i in range(2, len(x_values) - 2):
    f_prime.append(round(five_point_central_difference(f, x0+h*i, h), 4))

f_prime.append(round(five_point_backward_difference(f, xn-h, h), 4))
f_prime.append(round(five_point_backward_difference(f, xn, h), 4))

for i, x in enumerate(x_values):
    print(f"f'({x}) ≈ {f_prime[i]}")