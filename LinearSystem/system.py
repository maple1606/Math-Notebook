import numpy as np

A = np.array(
    [
        [10.0, -1.0, 2.0, 0.0],
        [-1.0, 11.0, -1.0, 3.0],
        [2.0, -1.0, 10.0, -1.0],
        [0.0, 3.0, -1.0, 8.0],
    ]
)

b = np.array([6.0, 25.0, -11.0, 15.0])

print("System of equations:")
for i in range(A.shape[0]):
    equation = ""
    for j in range(A.shape[1]):
        equation += f"{A[i][j]}*{j+1}"
        if j < A.shape[1] - 1:
            equation += " + "
    equation += f" = {b[i]}"
    print(equation)