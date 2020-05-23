import numpy as np
from scipy.integrate import solve_ivp

M = 1
G = 9.8

def ironball_position(theta, v0, k, deltat):
    position = np.zeros(2)
    ### v is current speed but not v0
    """
    def fvdp2_y(t,y):
        y0, y1 = y
        dydt = [y1, -k*(v0**2)/M*(y1/v0)-G]
        return dydt

    def fvdp2_x(t,x):
        x0, x1 = x
        dxdt = [x1, -k*(v0**2)/M*(x1/v0)]
        return dxdt
    """
    def f_grav(t, z):
        x, y, vx, vy = z
        v = (vx**2 + vy**2)**(1/2)
        dzdt = [vx, vy, -k*(v**2)/M*(vx/v), -k*(v**2)/M*(vy/v)-G]
        return dzdt

    x0, y0 = 0, 0
    #sol_y = solve_ivp(fvdp2_y, [0,10], [y0, v0*np.sin(theta)], t_eval=[deltat], method='RK45')
    #sol_x = solve_ivp(fvdp2_x, [0,10], [x0, v0*np.cos(theta)], t_eval=[deltat], method='RK45')
    #print(sol_y.y)
    #print(sol_x.y)
    sol = solve_ivp(f_grav, [0,100], [x0, y0, v0*np.cos(theta), v0*np.sin(theta)], t_eval=[deltat])

    #print(sol.y)
    position[0] = sol.y[0].item()
    position[1] = sol.y[1].item()
    return position

if __name__ == '__main__':
    #theta, v0, k, deltat = 0.923886, 143.086, 0.0010565, 1.58532
    theta, v0, k, deltat = 0.794602, 165.92, 0.00145019, 6.32501
    ret = ironball_position(theta, v0, k, deltat)
    print(ret)