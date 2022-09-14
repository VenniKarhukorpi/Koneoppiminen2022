import numpy as np
import matplotlib as plt

A = np.arange(25).reshape(5,5)
print(A)

B = A[:,1]
print(B)

C = A[:,3]
print(C)

D = A[4,:]
print(D)

E = A[1:4:2,0:3:2]
print(E)