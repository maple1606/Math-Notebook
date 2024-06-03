def normalize_vector(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm

def power_method(A, x0, tol=1e-10, max_iter=1000):
    xk = normalize_vector(x0)
    eigenvalue = 0

    for i in range(max_iter):
        yk = np.dot(A, xk)
        
        xk_new = normalize_vector(yk)
        eigenvalue_new = np.dot(xk_new.T, np.dot(A, xk_new)) / np.dot(xk_new.T, xk_new)
        if np.linalg.norm(xk_new - xk) < tol and abs(eigenvalue_new - eigenvalue) < tol:
            break
        
        xk = xk_new
        eigenvalue = eigenvalue_new

    return eigenvalue, xk