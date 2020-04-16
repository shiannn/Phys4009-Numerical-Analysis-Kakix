import math
import scipy.misc as misc
from scipy.misc import derivative

def func(x):
    value = 1.
    for n in range(1,4+1):
        value *= (math.cos(n*math.pi*x/2)*math.cosh(x) + math.sin(n*math.pi*x/2)*math.sinh(x))
    return value

def func_first_derivative(x):
    value = derivative(func, x, dx=1e-5)
    return value

if __name__=='__main__':
    x = 2
    ret = func_first_derivative(x)
    print(ret)
