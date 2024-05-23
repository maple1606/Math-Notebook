import numpy as np
from scipy.integrate import quad

def f(x):
    return np.sin(np.pi * x)

def polynomial_least_squares_regression(f, degree, a, b):
    A = np.zeros((degree + 1, degree + 1))
    for i in range(degree + 1):
        for j in range(degree + 1):
            integrand = lambda x: x**(i + j)
            A[i, j], _ = quad(integrand, a, b)
    
    b_vec = np.zeros(degree + 1)
    for i in range(degree + 1):
        integrand = lambda x: x**i * f(x)
        b_vec[i], _ = quad(integrand, a, b)
    
    coefficients = np.linalg.solve(A, b_vec)
    
    return coefficients

degree = 2

coefficients = polynomial_least_squares_regression(f, degree, 0, 1)

print(f"Coefficients: {coefficients}")

def predict(x, coefficients):
    return sum(c * x**i for i, c in enumerate(coefficients))

new_x = 0.5
predicted_y = predict(new_x, coefficients)
print(f"Predicted y for x = {new_x}: {predicted_y}")