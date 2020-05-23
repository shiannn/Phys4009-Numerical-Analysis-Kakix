import numpy as np

def func(x,a, b):
    return abs(np.sin(a*np.pi*x+b))

def generate_dist(a,b):
    data = np.random.rand(100000)
    y = np.random.rand(100000)
    data = data[y < func(data, a,b)]
    return data[:10000]

if  __name__ == '__main__':
    ret = generate_dist(3,2)
    print(ret)