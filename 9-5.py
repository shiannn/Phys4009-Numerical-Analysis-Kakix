import numpy as np

def best_threshold(A, B):
    maxSum = -1.
    T = 0.
    A = np.array(A)
    B = np.array(B)
    for i in np.arange(-4, 4, 0.01):
        #print(i)
        lenA = len(A[A < i])
        lenB = len(B[B > i])
        #print(lenA+lenB)
        if lenA+lenB >= maxSum:
            maxSum = lenA+lenB
            T = i
            #print(T)
        #print(lenA+lenB)
    #print(T)
    return float(round(T, 2))

if __name__ == '__main__':
    A = [-0.34651665, -0.78023398, -0.00635709, -1.67787095, -0.81929889, -1.6241986 ]
    B = [1.58285085, 0.27380551, 3.13924034, 1.07288369, 3.39195345, 3.01757924]
    ret = best_threshold(A,B)
    print(ret)