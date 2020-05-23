import numpy as np
from scipy.integrate import solve_ivp

def charge_on_capacitor(R, C, V, T):
    charge = np.zeros(8)
    def f_q(t, q):
        dqdt = V*np.exp(-t/T)/R - q/(R*C)
        return dqdt

    q0 = 0
    
    for deltat in range(1,8+1):
        sol = solve_ivp(f_q, [0,8], [q0], t_eval=[deltat])
        #print(sol.y.squeeze())
        charge[deltat-1] = sol.y.squeeze()
    return charge

if __name__ == '__main__':
    R, C, V, T = 193.606, 0.0118068, 1.75247, 2.5526
    ret = charge_on_capacitor(R, C, V, T)
    print(ret)