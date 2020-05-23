import numpy as np
from scipy.integrate import solve_ivp

m = 1
q = 1
def particle_positions(E, B):
    positions = np.zeros((8,3))

    Ex, Ey, Ez = E
    Bx, By, Bz = B
    def f_magnetic(t, Z):
        x, y, z, vx, vy, vz = Z
        v = np.array([vx, vy, vz])
        a = q/m * E + q/m * np.cross(v, B)
        ax, ay, az = a
        dZdt = [vx, vy, vz, ax, ay, az]
        return dZdt
    for i in range(1, 8+1):
        sol = solve_ivp(f_magnetic, [0,8], [0, 0, 0,0,0,0], t_eval=[i])
        #print(sol.y.T.squeeze())
        positions[i-1] = sol.y.T.squeeze()[:3]
    return positions

if __name__ == '__main__':
    E, B = np.array([-0.36069415, -0.07997872,  0.14886586]), np.array([0.01406784, 0.19204499, 0.37330767])
    ret = particle_positions(E, B)
    print(ret)
