import numpy as np

def f(x):
    ret = 1
    for n in range(1,4+1):
        temp = np.cos(n*np.pi*x/2)*np.cosh(x)+np.sin(n*np.pi*x/2)*np.sinh(x)
        ret *= temp
    
    return ret

def give_me_an_array(x):
    output = np.ones_like(x)
    vecf = np.vectorize(f)
    ret = vecf(x)
    return ret

if __name__ == '__main__':
    x = np.array([ 0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9])
    ret = give_me_an_array(x)
    print(ret)