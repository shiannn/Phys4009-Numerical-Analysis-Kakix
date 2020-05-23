import numpy as np
import scipy.optimize as opt

def func(x, tau, mu, sigma, M, N):
    return M*np.exp(-((x-mu)**2)/(2*sigma**2)) + N*np.exp(-x/tau)

def model(x, tau, mean, sigma, M, N):
    #xp = (x-xmin)/(xmax-xmin)
    expo = np.exp(-x/tau)
    gaussian = np.exp(-0.5*((x-mean)/sigma)**2)
    return M*gaussian + N*expo

def bestfit_parameters(vy):
    par = np.zeros(3)
    vx = np.linspace(0.01,1.99,100)
    vyerr = vy**0.5

    p_init = np.array([1.6, 1.0, 0.05, 1, 1])
    rx,rcov = opt.curve_fit(model, vx, vy, p_init, vyerr, bounds=(0,np.inf))

    return np.array(rx[:3]) 

if __name__ == '__main__':
    #vy = np.linspace(0.01,1.99,100)
    vy = np.array([71, 89, 70, 78, 66, 67, 82, 69, 82, 73, 92, 64, 75, 63, 70, 57, 65, 69,
61,  62,  63,  73,  61,  64,  60,  44,  73,  46,  49,  64,  63,  41,  42,  49,  54,  51,
  37,  39,  45,  53,  55,  69,  72,  87, 105, 102, 143, 182, 194, 186, 213, 174, 146, 111,
 117,  81,  57,  56,  37,  34,  40,  35,  41,  34,  29,  22,  34,  31,  23,  38,  15,  27,
  29,  25,  14,  14,  21,  22,  19,  18,  26,  30,  19,  22,  27,  21,  23,  23,  15,  22,
  16,  18,  14,  13,  11,  11,  11,  15,  17,  23])
    ret = bestfit_parameters(vy)
    print(ret)