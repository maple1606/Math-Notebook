import numpy as np
import matplotlib.pyplot as plt
from random import random
from math import sqrt 


class triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = (p1[0], p1[1])
        self.p2 = (p2[0], p2[1])
        self.p3 = (p3[0], p3[1])

R = 1
p1 = (R*random(), R*random())
p2 = (R*random(), R*random())
p3 = (R*random(), R*random())
sampleTriangle = triangle(p1, p2, p3)


def circumCirc(tri, display = True):
    ax, ay = tri.p1[0], tri.p1[1]
    bx, by = tri.p2[0], tri.p2[1]
    cx, cy = tri.p3[0], tri.p3[1]
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    c_x = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    c_y = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d

    radius = sqrt((c_x - ax)**2 + (c_y - ay)**2)

    if display:
        plt.figure(figsize=(4,4))
        plt.plot([ax,bx], [ay,by], 'ro-')
        plt.plot([cx,bx], [cy,by], 'ro-')
        plt.plot([ax,cx], [ay,cy], 'ro-')


        M = 1000
        angle = np.exp(1j * 2 * np.pi / M)
        angles = np.cumprod(np.ones(M + 1) * angle)
        x, y = c_x +  radius * np.real(angles), c_y + radius * np.imag(angles)
        plt.plot(x, y, c='b')
        plt.scatter([c_x], [c_y], s=25, c= 'b')

        plt.xlim([c_x - 1.2*radius, c_x + 1.2*radius])
        plt.ylim([c_y - 1.2*radius, c_y + 1.2*radius])
        plt.show()    

    return (round(c_x, 5), round(c_y, 5)), round(radius, 5)


print(circumCirc(sampleTriangle))