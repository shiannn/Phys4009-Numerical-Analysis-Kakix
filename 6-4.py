import math
import scipy.integrate as integrate

def standard(x):
    return (1/((2*math.pi)**(1/2)) * math.exp(-x**2/2))

def prob_at_nsigma(n):
    prob = integrate.quad(standard, -n, n)

    return prob[0]

if __name__ == '__main__':
    ret = prob_at_nsigma(2)
    print(ret)
