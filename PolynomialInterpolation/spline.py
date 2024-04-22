xp = 2.4

def find_interval(x, xp):
    # Find the index i such that x[i] <= xp < x[i+1]
    for i in range(len(x) - 1):
        if x[i-1] <= xp < x[i]:
            return i
    return None  # If xp is outside the range

def evaluate_cubic_spline(x, y, h, z, xp, i):
    # Evaluate the cubic spline at xp for the interval i
    C = (y[i] - y[i-1] + h**2 * (z[i-1]-z[i]) / 6) / h
    D = y[i-1] - h**2 * z[i-1] / 6
    result = z[i-1]*(x[i]-xp)**3 / (6*h) + z[i]*(xp-x[i-1])**3 / (6*h) + C*(xp-x[i-1]) + D
    return result

def tridiagonal_solver(a, b, c, d):
    n = len(d)
    w = np.zeros(n-1,float)
    g = np.zeros(n, float)
    p = np.zeros(n,float)
    
    w[0] = c[0]/b[0]
    g[0] = d[0]/b[0]

    for i in range(1,n-1):
        w[i] = c[i]/(b[i] - a[i-1]*w[i-1])
    for i in range(1,n):
        g[i] = (d[i] - a[i-1]*g[i-1])/(b[i] - a[i-1]*w[i-1])
    p[n-1] = g[n-1]
    for i in range(n-1,0,-1):
        p[i-1] = g[i-1] - w[i-1]*p[i]
    return p
    
def cubic_spline_interpolation(x, y, xp):
    # Given n+1 points
    n = len(x) - 1

    index = find_interval(x, xp)
    h = x[index] - x[index-1]
    
    z = np.zeros(n+1)
    z[0] = z[n] = 0 # Calculating natural cubic spline

    alpha = np.zeros(n)
    beta = np.zeros(n)
    b = np.zeros(n)
    
    b[1] = (y[2] - 2*y[1] + y[0])/h - h*z[0]/6
    b[n-1] = (y[n] - 2*y[n-1] + y[n-2])/h - h*z[n]/6 

    for i in range (1, n):
        alpha[i] = 2*h/3
        beta[i] = h/6
        if (i >= 2 and i < n-1):
            b[i] = (y[i+1] - 2*y[i] + y[i-1])/h

    z[1:-1] = tridiagonal_solver(beta[1:-1], alpha[1:], beta[1:-1], b[1:]) 
    
    return evaluate_cubic_spline(x, y, h, z, xp, index)
    
    
yp = cubic_spline_interpolation(x, y, xp)
yp = round(yp, 2)

plt.plot(x, y, 'o', label='Data points')
plt.plot(x_values, y_values, label='Fitted polynomial', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fitted Polynomial with cubic spline interpolation')
plt.legend()
plt.grid(True)

plt.plot(xp, yp, 'ko', label='Point (xp, yp)')
plt.text(xp, yp, f'({xp}, {yp})', ha='left')

plt.show()