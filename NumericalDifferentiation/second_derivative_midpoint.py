data = {
    1.20: 11.59006,
    1.29: 13.78176,
    1.30: 14.04276,
    1.31: 14.30741,
    1.40: 16.86187
}

def f(x):
    return data[round(x, 2)]

def central_difference_second_derivative(f, x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / h**2

h1 = 0.1
x = 1.3
f_double_prime_h1 = central_difference_second_derivative(f, x, h1)
print(f"f''(1.3) with h = 0.1: {round(f_double_prime_h1, 4)}")

h2 = 0.01
f_double_prime_h2 = central_difference_second_derivative(f, x, h2)
print(f"f''(1.3) with h = 0.01: {round(f_double_prime_h2, 4)}")