def bisection_method(f, a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        print("The function must have different signs at a and b.")
        return None
    
    iter_count = 0
    while (b-a) / 2.0 > tol and iter_count < max_iter:
        midpoint = (a+b) / 2.0
        if f(midpoint) == 0:
            return midpoint 
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        iter_count += 1
        
    return (a+b) / 2.0