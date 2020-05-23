import numpy as np
from scipy.integrate import solve_ivp

L0 = 1
k = 100
m1 = 0.5
m2 = 1.0

def twobody_positions(x1, y1, x2, y2, deltat):
    positions = np.zeros(4)

    def f_spring(t, z):
        x1, y1, x2, y2, vx1, vy1, vx2, vy2 = z
        L = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
        #dzdt = [vx, vy, -k*(v**2)/M*(vx/v), -k*(v**2)/M*(vy/v)-G]
        dzdt = [vx1, vy1, vx2, vy2, k/m1*(L-L0)*(x2-x1)/L, k/m1*(L-L0)*(y2-y1)/L, k/m2*(L-L0)*(x1-x2)/L, k/m2*(L-L0)*(y1-y2)/L]
        return dzdt

    sol = solve_ivp(f_spring, [0,100], [x1, y1, x2, y2, 0,0,0,0], t_eval=[deltat])
    positions[0] = sol.y[0].item()
    positions[1] = sol.y[1].item()
    positions[2] = sol.y[2].item()
    positions[3] = sol.y[3].item()
    #print(sol.y)
    return positions

if __name__ == '__main__':
    x1, y1, x2, y2, deltat = 0.976952, 0.609993, 1.76677, 1.49672, 4.84942
    ret = twobody_positions(x1, y1, x2, y2, deltat)
    print(ret)