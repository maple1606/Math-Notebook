def false_position_method(f, x0, x1, tol=1e-5, max_iter=100):
    f_x0 = f(x0)
    f_x1 = f(x1)
    if f_x0 * f_x1 > 0:
        raise ValueError("The function must have different signs at the endpoints a and b")

    for _ in range(max_iter):
        x2 = x1 - f_x1 * (x1-x0) / (f_x1-f_x0)
        f_x2 = f(x2)
        if abs(f_x2) < tol:
            return x2
        if f_x0 * f_x2 < 0:
            x1, f_x1 = x2, f_x2
        else:
            x0, f_x0 = x2, f_x2
    raise RuntimeError("False position method did not converge")