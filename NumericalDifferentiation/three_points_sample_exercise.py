data = {
    1.05: -1.709847, 
    1.10: -1.373823, 
    1.15: -1.119214, 
    1.20: -0.9160143, 
    1.25: -0.7470223, 
    1.30: -0.6015966
}

def f(x):
    return data[round(x, 2)]

h = 0.05
x0 = 1.05
xn = 1.30

f_prime = []
f_prime.append(round(three_point_forward_difference(f, x0, h), 4))

for i in range(1, len(x_values) - 1):
    f_prime.append(round(three_point_midpoint(f, x0 + h*i, h), 4))

f_prime.append(round(three_point_backward_difference(sample_function, xn, h), 4))

for i, x in enumerate(x_values):
    print(f"f'({x}) ≈ {f_prime[i]}")