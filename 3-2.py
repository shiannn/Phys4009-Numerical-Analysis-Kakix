import math
import numpy as np

def evaluate_equation(x,y,t):
    ret_value = 1.
    for n in range(1,4+1):
        temp  = math.cos(n*math.pi*t/2)*np.cosh(x)+math.sin(n*math.pi*t/2)*np.sinh(y)
        ret_value *= temp
    return ret_value

if __name__=='__main__':
    x=+0.8499 
    y=+0.2688 
    t=+0.8604
    ret = evaluate_equation(x,y,t)
    print(type(ret))
