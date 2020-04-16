import math
import scipy.integrate as integrate

def func(x):
    value = 0.
    for n in range(1,5+1):
        value += (1+math.sin(n*math.pi*x)*x+math.cos(n*math.pi*x)*(x**2))
    return value

def func_integrated(x):
    value = integrate.quad(func, -x, x)
    return value[0]

if __name__ == '__main__':
    ret = func_integrated(2)
    print(ret)
