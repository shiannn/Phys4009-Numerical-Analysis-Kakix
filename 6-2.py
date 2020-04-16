import math
import scipy.misc as misc
from scipy.misc import derivative

def func(x):
    value = x**2+math.exp(x)+math.log(x)+math.sin(x)
    return value

def func_2nd_derivative_numerical(x):
    return derivative(func, x, dx=1e-5, n=2)

def func_2nd_derivative_analytical(x):
    return 2+math.exp(x)-(1/x**2)-math.sin(x)

if __name__ == '__main__':
    retA = func_2nd_derivative_analytical(2)
    retN = func_2nd_derivative_numerical(2)
    print(retA)
    print(retN)
