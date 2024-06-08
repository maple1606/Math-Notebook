def adams_bashforth_4(f, y0, x0, x_end, h, initial_values):
    n = int((x_end - x0) / h)
    x = np.linspace(x0, x_end, n+1)
    y = np.zeros(n+1)
    
    y[:4] = initial_values
    
    for i in range(3, n):
        y[i+1] = y[i] + h * (55*f(x[i], y[i]) - 59*f(x[i-1], y[i-1]) + 37*f(x[i-2], y[i-2]) - 9*f(x[i-3], y[i-3])) / 24
    
    return x, y