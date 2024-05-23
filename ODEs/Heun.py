def heun_method(f, x0, y0, h, x_end):
    x_values = [x0]
    y_values = [y0]
    x = x0
    y = y0

    while x < x_end:
        y_predictor = y + h * f(x, y)
        y = y + 0.5 * h * (f(x, y) + f(x + h, y_predictor))
        x = x + h

        x_values.append(x)
        y_values.append(y)

    return x_values, y_values

x0 = 1
y0 = -4
h = 0.01   
x_end = 2.0

x_values, y_values = heun_method(f, x0, y0, h, x_end)

plt.plot(x_values, y_values, label='Heun\'s Predictor Corrector Method')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Heun\'s Predictor Corrector Method for Solving ODEs')
plt.legend()
plt.grid(True)
plt.show()