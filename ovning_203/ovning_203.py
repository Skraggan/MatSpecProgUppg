import numpy as np

def hitta_mista_kvadrat(X, Y):
    A = np.c_[np.ones(X.shape), X]
    return np.linalg.inv(A.T @ A) @ (A.T @ Y)

X = np.array([150, 250, 450, 600, 725])
Y = np.array([74.3, 127, 230, 289, 367])

m, k = hitta_mista_kvadrat(X, Y)
print(f"y = {k:.3f}x + {m:.3f}")



