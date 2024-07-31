def de_boor(k, x, t, c, p):
    d = [c[j + p - k] for j in range(0, k + 1)]
    for r in range(1, k + 1):
        for j in range(k, r - 1, -1):
            alpha = (x - t[j + p - k]) / (t[j + 1 + p - r] - t[j + p - k])
            d[j] = (1.0 - alpha) * d[j - 1] + alpha * d[j]
    return d[k]

control_points = np.array([[0, 0], [1, 2], [3, 5], [6, 5], [7, 2], [8, 0]])

k = 3

n = len(control_points)
knots = np.concatenate(([0]*k, np.linspace(0, 1, n - k + 1), [1]*k))

t_values = np.linspace(knots[k], knots[-k-1], 100)
spline_points = np.array([de_boor(k, t, knots, control_points, np.searchsorted(knots, t) - 1) for t in t_values])

plt.plot(control_points[:, 0], control_points[:, 1], 'o-', label='Control Points')
plt.plot(spline_points[:, 0], spline_points[:, 1], label='B-spline Curve')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('B-spline Curve using De Boor\'s Algorithm')
plt.grid(True)
plt.show()
