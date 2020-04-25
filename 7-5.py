import numpy as np
import scipy.linalg as linalg
from numpy.linalg import inv
from numpy.linalg import det

def give_me_an_array(A, B, C):
    output = np.zeros((2,2))
    output[0,0] = det(A+np.dot(B,inv(C)))
    output[0,1] = det(B-np.dot(C,inv(A)))
    output[1,0] = det(B-np.dot(A,inv(C)))
    output[1,1] = det(A+np.dot(C,inv(B)))

    return output

if __name__ == '__main__':
    A = np.array([[1., 2.],
           [3., 4.]])

    B = np.array([[3., 2.],
            [4., 1.]])

    C = np.array([[2., 4.],
            [1., 3.]])
    
    ret = give_me_an_array(A, B, C)
    print(ret)