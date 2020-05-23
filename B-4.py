import numpy as np
from scipy.stats import rv_continuous
import matplotlib.pyplot as plt

def func(x,T):
    return np.exp(-x/T)

def generate_dist(T,S):
    data = np.random.rand(10000)
    col = []
    x = np.random.exponential(T,size=10000)
    mu = x
    sigma = S*x
    #print(mu)
    #print(sigma)
    ret = np.random.normal(mu, sigma)
    #print(ret)

    return ret

if __name__ == '__main__':
    ret = generate_dist(1.5,1.2)
    print(ret)
"""
#print(gaussian.rvs(size=10))
plt.hist(gaussian.rvs(size=200))
plt.show()
"""