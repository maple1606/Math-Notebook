xp = 2.4

def newtonCoefficients(x, y):
    f = np.zeros((n, n))

    # construct the divided difference table
    for i in range(n):
        f[i, 0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            f[i, j] = (f[i+1, j-1] - f[i, j-1]) / (x[i+j] - x[i])   
    # print(f)
  
    coefficients = np.zeros(n)
    for i in range(0, n):
        coefficients[i] = f[0, i]
    return coefficients

def evaluate(x, y, xp):
    coefficients = newtonCoefficients(x, y)
    n = len(coefficients)
    yp = coefficients[0]
    for i in range(1, n):
        term = coefficients[i]
        for j in range(i):
            term *= (xp - x[j])
        yp += term
    return yp

yp = evaluate(x, y, xp)

plt.plot(x, y, 'o', label='Data points')
plt.plot(x_values, y_values, label='Fitted polynomial', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fitted Polynomial with Newton interpolation')
plt.legend()
plt.grid(True)

plt.plot(xp, yp, 'ko', label='Point (xp, yp)')
plt.text(xp, yp, f'({xp}, {yp})', ha='left')

plt.show()