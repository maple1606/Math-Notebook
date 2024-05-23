import numpy as np
from tabulate import tabulate

x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([1.5, 3.8, 6.7, 9.0, 11.2, 13.6, 16])

def discrete_least_squares_regression(x, y):
    x = np.array(x)
    y = np.array(y)

    n = len(x)

    x_sum = np.sum(x)
    y_sum = np.sum(y)
    xy_sum = np.sum(x * y)
    x2_sum = np.sum(x**2)

    a0 = (x2_sum * y_sum - xy_sum * x_sum) / (n * x2_sum - x_sum ** 2)
    a1 = (n * xy_sum - x_sum * y_sum) / (n * x2_sum - x_sum ** 2)
    
    return a1, a0

a1, a0 = discrete_least_squares_regression(x, y)

print(f"Slope (a1): {round(a1, 4)}")
print(f"Intercept (a0): {round(a0, 4)}\n")

cmp = []
err = 0

for curr_x, curr_y in zip(x, y):
    predicted_y = a1 * curr_x + a0
    err = err + (curr_y - predicted_y) ** 2
    cmp.append([curr_y, round(predicted_y, 2)])

print(tabulate(cmp, headers=["Initial y", "Predicted y"]))
print("\n=> Error:", round(err, 2))