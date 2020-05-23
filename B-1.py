import numpy as np

def func(x,a):
    return 1 / (1+a*x)

def generate_dist(a):
    data = np.random.rand(100000)
    y = np.random.rand(100000)
    data = data[y < func(data, a)]
    return data[:10000]

if  __name__ == '__main__':
    ret = generate_dist(0.1)
    print(ret)