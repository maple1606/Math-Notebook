def newton_method(f, df, x0, tol=1e-5, max_iter=100):
    x = x0
    for _ in range(max_iter):
        f_x = f(x)
        if abs(f_x) < tol:
            return x
        x = x - f_x / df(x)
    raise RuntimeError("Newton's method did not converge")