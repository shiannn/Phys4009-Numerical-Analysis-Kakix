import math
import scipy.integrate as integrate
from scipy import optimize

def standard(x):
    return (1/((2*math.pi)**(1/2)) * math.exp(-x**2/2))

def prob_at_nsigma_90(n):
    prob = integrate.quad(standard, -n, n)

    return (prob[0]-0.9)

def prob_at_nsigma_95(n):
    prob = integrate.quad(standard, -n, n)

    return (prob[0]-0.95)

result90 = optimize.root(prob_at_nsigma_90 , x0 = [2], tol=1e-2)
#print(result90.x)
result95 = optimize.root(prob_at_nsigma_95 , x0 = [2], tol=1e-2)
#print(result95.x)

n_sigma_at_90percent = result90.x
n_sigma_at_95percent = result95.x

print('Probability of 90%% = %3.2f sigma' % n_sigma_at_90percent)
print('Probability of 95%% = %3.2f sigma' % n_sigma_at_95percent)
