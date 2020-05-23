import numpy as np
from scipy.integrate import tplquad

def func(r,theta,phi,A,B,C):
    return A*(r**3)+B*(r**2)*np.sin(theta)*np.sin(phi)+C*r*np.cos(theta)*np.cos(phi)

def func_integration(A,B,C):
    numTrails = 10000
    result = 0.
    """
    A = A*np.ones(numTrails)
    B = B*np.ones(numTrails)
    C = C*np.ones(numTrails)

    r = np.random.uniform(0,1,numTrails)
    theta = np.random.uniform(0,np.pi,numTrails)
    phi = np.random.uniform(0,2*np.pi,numTrails)

    #print(x,y,z,P,Q)
    ret = func(r,theta,phi,A,B,C)
    result = ret.mean()*1*np.pi*2*np.pi
    print(result)
    """
    #return float(result)
    Function = lambda phi, theta, r: A*(r**3)+B*(r**2)*np.sin(theta)*np.sin(phi)+C*r*np.cos(theta)*np.cos(phi)
    r1, r2 = 0, 1
    theta1, theta2 = lambda r: 0, lambda r: np.pi
    phi1, phi2 = lambda r, theta:0, lambda r, theta: 2*np.pi
    vals = tplquad(
        Function,  r1, r2, theta1, theta2, phi1, phi2
    )
    print(vals)
    return vals[0]

def monteCarlo(A,B,C):
    numTrails = 40000
    result = 0.
    
    A = A*np.ones(numTrails)
    B = B*np.ones(numTrails)
    C = C*np.ones(numTrails)

    r = np.random.uniform(0,1,numTrails)
    theta = np.random.uniform(0,np.pi,numTrails)
    phi = np.random.uniform(0,2*np.pi,numTrails)

    #print(x,y,z,P,Q)
    ret = func(r,theta,phi,A,B,C)
    result = ret.mean()*1*np.pi*2*np.pi
    print(result)
    

if __name__ == '__main__':
    ret = func_integration(1.58091, 0.666744, 0.553217)
    monteCarlo(1.58091, 0.666744, 0.553217)
    #F(x) expected=+3.3119e+00(+-0.14%) result=+7.8015e+00
    print(ret)
