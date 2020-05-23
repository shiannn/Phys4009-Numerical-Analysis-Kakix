import numpy as np

def func(XY,a,b):
    x = XY[:,0]
    y = XY[:,1]
    #print(x)
    #print(y)
    return x*y*(1-a*x)*(1-b*y)

def generate_dist(a,b):
    data = np.random.rand(200000,2)
    ztarget = np.random.rand(200000)
    #print(data)
    Z = func(data,a,b)
    #print(Z)
    #print(ztarget)
    data = data[ztarget<Z]
    return data[:10000]

if __name__ == '__main__':
    ret = generate_dist(0,1)
    print(ret)
    print(len(ret))