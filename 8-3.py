import numpy as np

def cov_to_corr(covariance):
    correlation = covariance.copy()
    v = np.sqrt(np.diag(covariance))
    outer_v = np.outer(v, v)
    correlation = covariance / outer_v
    correlation[covariance == 0] = 0
    return correlation

if __name__ == '__main__':
    covariance = np.array([
        [1,5],
        [3,4]
    ])
    ret = cov_to_corr(covariance)
    print(ret)