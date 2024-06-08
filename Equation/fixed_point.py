def fixed_point_iteration(x0, tol, max_iterations=1000):
    x_current = x0
    for iteration in range(max_iterations):
        x_next = g(x_current)
        if abs(x_next - x_current) < tol:
            return x_next, iteration + 1
        x_current = x_next
    return x_current, max_iterations