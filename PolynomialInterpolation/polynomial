import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt

x = np.array([1, 2, 3])
y = np.array([2, 3, 6])

n = len(x)
coefficients = np.polyfit(x, y, 2)
p = np.poly1d(coefficients)

x_values = np.linspace(min(x), max(x))

y_values = p(x_values)

plt.plot(x, y, 'o', label='Data points')
plt.plot(x_values, y_values, label='Fitted polynomial', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fitted Polynomial')
plt.legend()
plt.grid(True)
plt.show()