def secant_method(f, x0, x1, tol=1e-5, max_iter=100):
    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        if abs(f_x1) < tol:
            return x1
        x2 = x1 - f_x1 * (x1-x0) / (f_x1 - f_x0)
        x0, x1 = x1, x2
    raise RuntimeError("Secant method did not converge")