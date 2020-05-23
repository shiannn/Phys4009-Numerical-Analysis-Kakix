import numpy as np

def func(x,y,z,P,Q):
    return np.sin((x+y)/P)*np.sin((y+z)/P)*np.sin((z+x)/P) / np.exp(-x*y*z/Q)

def func_integration(P,Q):
    numTrails = 10000
    result = 0.
    trail = np.random.uniform(0,np.pi,(numTrails,3))
    P = P*np.ones(numTrails)
    Q = Q*np.ones(numTrails)
    x = trail[:,0]  
    y = trail[:,1]  
    z = trail[:,2]  

    #print(x,y,z,P,Q)
    ret = func(x,y,z,P,Q)
    #print(ret.mean())
    result = ret.mean()*np.pi*np.pi*np.pi
    return float(result)

if __name__ == '__main__':
    ret = func_integration(1,2)
    print(ret)
