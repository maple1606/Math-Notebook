def runge_kutta_4(f, x0, y0, h, x_end):
    x_values = [x0]
    y_values = [y0]
    x = x0
    y = y0

    while x < x_end:
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1 * h)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2 * h)
        k4 = h * f(x + h, y + k3 * h)
        
        x = x + h
        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

        x_values.append(x)
        y_values.append(y)

    return x_values, y_values

x0 = 1
y0 = -4
h = 0.01   
x_end = 2.0

x_values, y_values = runge_kutta_4(f, x0, y0, h, x_end)

plt.plot(x_values, y_values, label='RK4 Method')
plt.xlabel('x')
plt.ylabel('y')
plt.title('RK4 Method for Solving ODEs')
plt.legend()
plt.grid(True)
plt.show()