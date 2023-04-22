# Write a function that takes two NumPy arrays A and b, where A is a square matrix and b is a column vector, 
# and solves the linear system Ax = b using LU decomposition.
import numpy as np
import scipy

def lu_solve(A, b):
    # LU decomposition of A
    P, L, U = scipy.linalg.lu(A)
    
    # Solve Ly = Pb using forward substitution
    Pb = np.dot(P, b)
    y = scipy.linalg.solve_triangular(L, Pb, lower=True)
    
    # Solve Ux = y using backward substitution
    x = scipy.linalg.solve_triangular(U, y, lower=False)
    
    return x


# Write a function that takes a NumPy array A and a column vector b, and solves the linear system Ax = b using Cholesky decomposition.


import scipy.linalg

def cholesky_solve(A, b):
    # Cholesky decomposition of A
    L = np.linalg.cholesky(A)
    
    # Solve Ly = b using forward substitution
    y = scipy.linalg.solve_triangular(L, b, lower=True)
    
    # Solve L.T x = y using backward substitution
    x = scipy.linalg.solve_triangular(L.T, y, lower=False)
    
    return x
A = np.array([[4, 2, 1], [2, 5, 3], [1, 3, 6]])
b = np.array([[1], [2], [3]])
x = cholesky_solve(A, b)
print(x)

# Write a function that takes two NumPy arrays A and b, where A is a square matrix and b is a column vector, 
# and solves the linear system Ax = b using QR decomposition.
from numpy.linalg import qr
def qr_solve(A, b):
    Q, R = qr(A)
    y = np.dot(Q.T, b)
    x = np.linalg.solve(R, y)
    return x

# Write a function that takes a NumPy array A and a column vector b, 
# and solves the linear system Ax = b using singular value decomposition (SVD).

def svd_solve(A, b):
    U, S, V_T = np.linalg.svd(A)
    S_inv = np.diag(1.0 / S)
    x = V_T.T @ S_inv @ U.T @ b
    return x
# Write a function that takes a NumPy array A and a column vector b, and solves the linear system Ax = b using iterative methods such as Jacobi or Gauss-Seidel.

def jacobi_solve(A, b, tol=1e-10, max_iter=1000):
    n = len(A)
    x = np.zeros(n)
    D = np.diag(A)
    R = A - np.diagflat(D)
    for i in range(max_iter):
        x_new = (b - np.dot(R, x)) / D
        if np.linalg.norm(x_new - x) < tol:
            return x_new
        x = x_new
    raise Exception("Jacobi method did not converge")


