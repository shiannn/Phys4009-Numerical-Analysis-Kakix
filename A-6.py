import numpy as np
from scipy.integrate import solve_ivp

def current_on_circuit(R, L, C, I0):
    current = np.zeros(8)

    def f_I(t, z):
        I, dIdt = z
        dI2d2t = -R/L*dIdt - I/(L*C)
        dzdt = [dIdt, dI2d2t]
        return dzdt

    dIdt0 = 0
    for deltat in range(1,8+1):
        sol = solve_ivp(f_I, [0,8], [I0, dIdt0], t_eval=[deltat])
        #print(sol.y[0].squeeze())
        current[deltat-1] = sol.y[0].squeeze()

    return current

if __name__ == '__main__':
    R, L, C, I0 = 130.954, 3.70024, 0.0127709, 0.155162
    ret = current_on_circuit(R, L, C, I0)
    print(ret)