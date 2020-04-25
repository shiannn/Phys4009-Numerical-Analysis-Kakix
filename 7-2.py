import numpy as np

def func2(i,j):
    return i+j+1

def give_me_an_array(n):
    output = np.zeros((n,n), dtype='int64')
    output = np.fromfunction(func2, (n,n), dtype=int)
    return output

if __name__ == '__main__':
    ret = give_me_an_array(10)
    print(ret)