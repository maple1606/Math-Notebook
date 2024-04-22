def jacobi(A, b):
    TOLERANCE = 1e-8
    ITERATION_LIMIT = 1000

    x = np.zeros_like(b)
    n = len(b)
    x_new = np.zeros_like(x)
    for _ in range(ITERATION_LIMIT):
        for i in range(n):
            x_new[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
        if np.linalg.norm(x_new - x, ord=np.inf) < TOLERANCE:
            break
        x = np.copy(x_new)
    return x

solution = jacobi(A, b)
print("Solution:")
print(solution)
