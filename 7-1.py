import numpy as np

def func2(i,j):
    #return (i==j+1 or i==j-1 or i==9-j-1 or i==9-j+1)
    temp = np.logical_or(i==j+1, i==j-1)
    temp = np.logical_or(temp, i==9-j-1)
    temp = np.logical_or(temp, i==9-j+1)
    #print('i', temp)
    return temp
    #return (i==j+1 or i==j)

def give_me_an_array(n):
    output = np.zeros((10,10), dtype='int64')
    mask = np.fromfunction(func2, (10,10), dtype=int)
    output = np.where(mask, np.ones(output.shape)*n, np.zeros(output.shape))
    return output

if __name__ == '__main__':
    ret = give_me_an_array(5)
    print(ret)