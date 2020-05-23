import numpy as np
import scipy.optimize as opt

def func(t,a,b,c):
    return a + b*t + c*(t**2)

def errorSum(coeff,X,dX):
    a, b, c = coeff
    ret = 0
    for t in range(10):
        ret += ((func(t,a,b,c) - X[t])/dX[t])**2
    return ret

def bestfit_parameters(x, dx):
    par = np.zeros(3)
    root = opt.minimize(errorSum, x0=[0,0,0], args=(x,dx), tol=1e-9)
    print(np.array(root.x))
    return np.array(root.x)

if __name__ == '__main__':
    x = np.array([0.69748453, 3.24160366, 7.562668, 15.08621815, 24.11790529, 
    35.93666222, 49.84321195, 66.08141961, 86.00257091, 106.59033617])
    dx = np.array([0.33255298, 0.25390351, 0.3417747, 0.35645815, 0.29287464, 0.22741397, 
    0.39971765, 0.3605281, 0.38427792, 0.37053421])
    bestfit_parameters(x,dx)
