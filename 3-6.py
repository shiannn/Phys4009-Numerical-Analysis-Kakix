def legendre(n, x):
    if(n==0):
        return 1
    elif(n==1):
        return x
    elif(n==2):
        return 1/2*(3*x**2-1)
    elif(n==3):
        return 1/2*(5*x**3-3*x)