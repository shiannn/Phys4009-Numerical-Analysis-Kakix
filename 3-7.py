def legendre(n, x):
    if(n==0):
        return 1.
    if(n==1):
        return x
    temp = (2*n-1)*x*legendre(n-1,x)-(n-1)*legendre(n-2,x)
    return temp/n
