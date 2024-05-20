def gauss_seidel(A, b):
    TOLERANCE = 1e-8
    ITERATION_LIMIT = 1000

    x = np.zeros_like(b)
    n = len(b)
    
    while ITERATION_LIMIT > 0:
        ITERATION_LIMIT -= 1
        x_old = np.copy(x)
        for i in range(n):
            x[i] = (b[i] - (np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x_old[i+1:]))) / A[i, i]
        if np.linalg.norm(x - x_old, ord=np.inf) < TOLERANCE:
            break
    return x

solution = gauss_seidel(A, b)
print("Solution using Gauss-Seidel iteration:")
print(solution)