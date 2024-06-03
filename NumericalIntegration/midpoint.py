def midpoint_rule(f, a, b, n):
    h = (b-a) / n
    x = np.linspace(a+h/2, b-h/2, n)
    y = f(x)
    integral = h * np.sum(y)
    return integral

# Part (a)
f_a = lambda x: (np.cos(x))**2
a_a, b_a = -0.25, 0.25
integral_a = midpoint_rule(f_a, a_a, b_a, 4)

# Part (b)
f_b = lambda x: x * np.log(x+1)
a_b, b_b = -0.5, 0
integral_b = midpoint_rule(f_b, a_b, b_b, 4)

# Part (c)
f_c = lambda x: (np.sin(x))**2 - 2*x * np.sin(x) + 1
a_c, b_c = 0.75, 1.3
integral_c = midpoint_rule(f_c, a_c, b_c, 4)

# Part (d)
f_d = lambda x: 1 / (x*np.log(x))
a_d, b_d = np.e, np.e + 1
integral_d = midpoint_rule(f_d, a_d, b_d, 4)

print("a:", round(integral_a, 4))
print("b:", round(integral_b, 4))
print("c:", round(integral_c, 4))
print("d:", round(integral_d, 4))