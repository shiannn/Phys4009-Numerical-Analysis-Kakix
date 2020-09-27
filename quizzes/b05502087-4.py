import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def hist_fit(hist):
    ret = np.array([100.,1.,0.05])
    ### START YOUR CODE HERE ###
    xmin, xmax, xbinwidth = 0., 2., 0.02
    vx = np.linspace(xmin+xbinwidth/2,xmax-xbinwidth/2,100)
    vy = hist
    vyerr = vy**0.5
    print(vx)
    print(vy)
    print(vyerr)

    def plotHist(N,mu,sigma):
        xmin, xmax, xbinwidth = 0., 2., 0.02
        cx = np.linspace(xmin,xmax,500)
        cy = N*xbinwidth/(2.*np.pi)**0.5/sigma * np.exp(-0.5*((cx-mu)/sigma)**2)
        plt.plot(cx, cy, c='red',lw=2)
    
    def plotexp(N,tau):
        xmin, xmax, xbinwidth = 0., 2., 0.02
        cx = np.linspace(xmin,xmax,500)
        cy = N*np.exp((-1)*cx/tau)
        plt.plot(cx, cy, c='red',lw=2)

    def model(x, norm1, norm2, norm3, norm4, mean1, sigma1, tau):
        xbinwidth = 0.02
        mean2 = 0.1
        mean3 = 0.7
        sigma2 = 0.4
        sigma3 = 0.2

        #plotHist(norm2, mean2, sigma2)
        #plotHist(norm3, mean3, sigma3)
        #plotHist(norm1, mean1, sigma1)
        

        gaussian1 = norm1*xbinwidth/(2.*np.pi)**0.5/sigma1 * np.exp(-0.5*((x-mean1)/sigma1)**2)
        gaussian2 = norm2*xbinwidth/(2.*np.pi)**0.5/sigma2 * np.exp(-0.5*((x-mean2)/sigma2)**2)
        gaussian3 = norm3*xbinwidth/(2.*np.pi)**0.5/sigma3 * np.exp(-0.5*((x-mean3)/sigma3)**2)
        expo = norm4*np.exp(-x/tau)

        #plotexp(norm4, tau)
        #plt.show()

        return gaussian1+gaussian2+gaussian3+expo
    
    def fcn(p):
        expt = model(vx,p[0],p[1],p[2],p[3],p[4],p[5], p[6])
        delta = (vy-expt)/vyerr

        return (delta**2).sum()
    
    p_init = np.array([1000,800,600,110,1,0.06,0.9999]) 
    res = opt.minimize(fcn,p_init) 
    norm1, norm2, norm3, norm4, mean1, sigma1, tau = res.x

    ret = np.array([norm1,mean1,sigma1])
    
    
    #### END YOUR CODE HERE ####
    return ret

if __name__ == '__main__':
    data = np.load('hist_data.npy')
    
    idx = np.random.randint(50)
    idx = 0
    ret = hist_fit(data[idx])
    
    print('Signal main Gaussian parameters:')
    print('Area: %.1f' % ret[0])
    print('Mean: %.4f' % ret[1])
    print('Sigma: %.4f' % ret[2])
    
    xmin, xmax, xbinwidth = 0., 2., 0.02
    vx = np.linspace(xmin+xbinwidth/2,xmax-xbinwidth/2,100)
    vy = data[idx]
    vyerr = vy**0.5

    fig = plt.figure(figsize=(6,6), dpi=80)
    plt.errorbar(vx, vy, vyerr, c='blue', fmt = '.')

    N,mu,sigma = ret[0],ret[1],ret[2]
    cx = np.linspace(xmin,xmax,500)
    cy = N*xbinwidth/(2.*np.pi)**0.5/sigma * np.exp(-0.5*((cx-mu)/sigma)**2)
    plt.plot(cx, cy, c='red',lw=2)

    plt.plot([xmin, xmax],[0.,0.],c='gray',lw=2)
    plt.grid()
    plt.show()