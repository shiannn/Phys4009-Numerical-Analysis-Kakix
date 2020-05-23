import numpy as np
import scipy.optimize as opt

def func(x, N):
    f_value = 0.
    sumX = sum([x**n for n in range(1,N+1)])
    f_value = sumX - N/2
    return float(f_value)

def func_prime(x, N):
    fp_value = 0.
    sumX = sum([n*x**(n-1) for n in range(1,N+1)])
    fp_value = sumX

    return float(fp_value)

def find_the_root(N):
    solution = 0.5
    root = opt.newton(func, 0.5, fprime=func_prime, args=(N,))
    solution = root
    return float(solution)

if __name__ == '__main__':
    ret = find_the_root(10)
    print(ret)
