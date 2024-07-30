# Reference: https://qroph.github.io/2018/07/30/smooth-paths-using-catmull-rom-splines.html

def catmull_rom_spline(P0, P1, P2, P3, n_points=100):
    t = np.linspace(0, 1, n_points)
    t2 = t**2
    t3 = t**3
    
    b0 = 0.5 * (-t3 + 2*t2 - t)
    b1 = 0.5 * (3*t3 - 5*t2 + 2)
    b2 = 0.5 * (-3*t3 + 4*t2 + t)
    b3 = 0.5 * (t3 - t2)
    
    x = b0*P0[0] + b1*P1[0] + b2*P2[0] + b3*P3[0]
    y = b0*P0[1] + b1*P1[1] + b2*P2[1] + b3*P3[1]
    
    return x, y

control_points = np.array([
    [0, 0],
    [1, 2],
    [3, 3],
    [4, 0],
])

spline_points_x = []
spline_points_y = []
P0 = control_points[0]
P1 = control_points[1]
P2 = control_points[2]
P3 = control_points[3]
x, y = catmull_rom_spline(P0, P1, P2, P3)

plt.plot(control_points[:, 0], control_points[:, 1], 'ro-', label='Control Points')
plt.plot(x, y, 'b-', label='Catmull-Rom Spline')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Catmull-Rom Spline')
plt.grid(True)
plt.show()