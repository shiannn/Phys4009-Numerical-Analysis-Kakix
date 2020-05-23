import numpy as np

def countZ(lenA, lenB):
    if lenA+lenB == 0:
        return -1
    return lenA / ((lenA+lenB)**(1/2))

def best_bounds(A, B):
    A = np.array(A)
    B = np.array(B)
    maxZ = -1
    bounds = np.array([-1.,1.])
    for j in np.arange(-3,3,0.1):
        for i in np.arange(-3,j,0.1):
            lenA = len(A[(A>i) & (A<j)])
            lenB = len(B[(B>i) & (B<j)])
            Z = countZ(lenA, lenB)
            if Z > maxZ:
                maxZ = Z
                bounds[0] = i
                bounds[1] = j
            
    return bounds.round(1)
