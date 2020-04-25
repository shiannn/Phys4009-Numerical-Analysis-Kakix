import numpy as np
import scipy.linalg as linalg

def give_me_an_array(b):
    N = b.shape[0]
    output = np.zeros_like(b)
    upper = np.triu(np.ones(N))
    A = upper+np.eye(N)
    x = np.linalg.solve(A,b)
    #print(x)
    return x

if __name__ == '__main__':
    b = np.array([[ 4. ],
           [ 3. ],
           [ 2. ],
           [ 1. ]])

    ret = give_me_an_array(b)
    print(ret)