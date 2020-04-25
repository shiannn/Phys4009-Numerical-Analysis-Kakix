import numpy as np

def give_me_an_array(A, B, C):
    #output = np.zeros_like(A)
    N = A.shape[0]
    output = np.dot(A,A)+ np.dot(B,B)+np.dot(C,C) - np.dot(A,B) - np.dot(B,C) - np.dot(C,A) + 4*np.eye(N)

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