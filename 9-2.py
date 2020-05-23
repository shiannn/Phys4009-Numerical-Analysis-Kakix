import numpy as np
import scipy.optimize as opt
import warnings
warnings.filterwarnings("error")

def func(x, t):
    f_value = 0.
    f_value = abs(np.sin(x)/((x/2/np.pi)**x+np.pi/8)) - x / (2*np.pi) + (x / (2*np.pi))**2 - t/4
    return float(f_value)

def find_the_roots(t):
    ans = []
    solutions = []
    for st in np.arange(0,10,0.2):
        try:
            ret = opt.fsolve(func, [st], args=t)
            solutions.append(ret.item())
        except:
            pass
    solutions = sorted(solutions)
    for i, s in enumerate(solutions):
        if i==0 or (abs(solutions[i] - solutions[i-1]) > 0.5):
            ans.append(solutions[i])
    return np.array(ans)

if __name__ == '__main__':
    #ret = func(np.array([2,5]),2)
    ret = find_the_roots(1.5048)
    print(ret)