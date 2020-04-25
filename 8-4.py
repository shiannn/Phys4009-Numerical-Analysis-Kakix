import numpy as np

def get_covariance(X,Y):
    covariance = np.ones((2,2))
    print(X,Y)
    print(X.mean())
    print(Y.mean())
    covariance[0,0] = ((X-X.mean())*(X-X.mean())).mean()
    covariance[0,1] = ((X-X.mean())*(Y-Y.mean())).mean()
    covariance[1,0] = ((Y-Y.mean())*(X-X.mean())).mean()
    covariance[1,1] = ((Y-Y.mean())*(Y-Y.mean())).mean()
    return covariance

if __name__ == '__main__':
    X = np.random.rand(5)
    Y = np.random.rand(5)
    ret = get_covariance(X,Y)
    print(ret)