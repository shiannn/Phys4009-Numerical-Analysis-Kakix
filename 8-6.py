import numpy as np
from numpy.linalg import inv
import scipy.linalg as linalg

def chisquare_search(Y):
    X = np.array([1.00,2.00,3.00,4.00,5.00])
    S = np.array([[0.62,0.21,0.12,0.04,0.09],
                  [0.21,0.78,0.32,0.10,0.12],
                  [0.12,0.32,0.69,0.03,0.15],
                  [0.04,0.10,0.03,0.95,0.20],
                  [0.09,0.12,0.15,0.20,0.83]])
    best_a,best_b = 0.,0.

    A = [0,0.2,-0.2,0.4,-0.4,0.6,-0.6,0.8,-0.8,1.0,-1.0]
    B = [0,0.2,-0.2,0.4,-0.4,0.6,-0.6,0.8,-0.8,1.0,-1.0]
    chisq = np.inf
    for a in A:
        for b in B:
            F = a*X+b
            temp = (Y - F).dot(inv(S)).dot((Y - F).T)
            print(temp)
            if temp.item() < chisq:
                chisq = temp.item()
                best_a = a
                best_b = b

    return np.array([best_a,best_b])

if __name__ == '__main__':
    Y = np.random.rand(5)
    ret = chisquare_search(Y)
    print(ret)