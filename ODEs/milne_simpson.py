def milne_simpson(f, y0, t0, t_end, h, initial_values):
    n_steps = int((t_end - t0) / h)
    t = np.linspace(t0, t_end, n_steps + 1)
    y = np.zeros(n_steps + 1)
    
    y[:4] = initial_values

    for i in range(2, n_steps):
        y_pred = y[i-3] + 4 * h * (2 * f(t[i-2], y[i-2]) - f(t[i-1], y[i-1]) + 2 * f(t[i], y[i])) / 3
        y_corr = y[i-1] + h * (f(t[i-1], y[i-1]) + 4 * f(t[i], y[i]) + f(t[i+1], y_pred)) / 3
        y[i + 1] = y_corr

    return t, y