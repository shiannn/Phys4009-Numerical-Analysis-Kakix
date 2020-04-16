import math
import scipy.integrate as integrate

def convoluted_BreitWigner(E, M, Gamma, sigma):
    breitWigner = lambda x,E,M,Gamma:(1/(((E-x)**2-M**2)**2+M**2*Gamma**2)*(math.exp(-x**2/(2*sigma**2))))
    y, err = integrate.quad(breitWigner, -3*sigma, 3*sigma, args=(E,M,Gamma))
    return y

if __name__ == '__main__':
