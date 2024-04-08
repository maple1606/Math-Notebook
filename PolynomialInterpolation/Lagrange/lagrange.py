xp = 2.4

def evaluate(x, y, xp):
    yp = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p = p * (xp - x[j]) / (x[i] - x[j])
        yp = yp + y[i] * p
    return yp

yp = evaluate(x, y, xp)
yp = round(yp, 2)
print(yp)

plt.plot(x, y, 'o', label='Data points')
plt.plot(x_values, y_values, label='Fitted polynomial', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fitted Polynomial with Lagrange interpolation')
plt.legend()
plt.grid(True)

plt.plot(xp, yp, 'ko', label='Point (xp, yp)')
plt.text(xp, yp, f'({xp}, {yp})', ha='left')

plt.show()