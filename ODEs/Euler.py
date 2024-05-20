def euler_method(f, x0, y0, h, x_end):
    x_values = [x0]
    y_values = [y0]
    x = x0
    y = y0
    
    while x < x_end:
        y = y + h * f(x, y)
        x = x + h
        
        x_values.append(x)
        y_values.append(y)
    
    return x_values, y_values

x0 = 1
y0 = -4
h = 0.01   
x_end = 2.0

x_values, y_values = euler_method(f, x0, y0, h, x_end)

# for x, y in zip(x_values, y_values):
#     print(f"x: {x:.2f}, y: {y:.4f}")

plt.plot(x_values, y_values, label='Euler Method')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Euler Method for Solving ODEs')
plt.legend()
plt.grid(True)
plt.show()