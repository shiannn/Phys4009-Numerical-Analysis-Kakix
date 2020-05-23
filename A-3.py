import numpy as np
from scipy.integrate import solve_ivp

# in the order of [mass, x, y, vx, vy]
init_data = np.array([[0.362, +0.380, -1.954, -2.364, +0.461],
                      [0.168, +0.032, +0.631, +0.233, -0.608],
                      [0.413, +0.280, -0.095, -0.672, -0.369],
                      [0.209, -1.669, +0.116, -1.965, +0.237],
                      [0.172, +0.376, +0.673, -0.370, +0.723],
                      [0.322, -0.583, +0.355, -0.405, +0.831],
                      [0.289, -0.619, -0.960, -0.525, -1.366],
                      [0.108, +0.626, -1.931, +0.276, +1.698],
                      [0.491, +0.499, +0.217, -1.237, +0.084],
                      [0.325, +0.781, +1.452, -0.295, -0.827]])

def multibody_positions(deltat):
    positions = np.zeros((10,2))
    def f_particles(t, z):
        inpu = z.reshape(-1,5)
        m = inpu[:,0]
        x = inpu[:,1]
        y = inpu[:,2]
        vxret = inpu[:,3]
        vyret = inpu[:,4]
        
        axret = np.zeros(10)
        ayret = np.zeros(10)
        """
        for i in range(len(inpu)):
            for j in range(len(inpu)):
                if i!=j:
                    Rij = ((x[i]-x[j])**2+(y[i]-y[j])**2)**(1/2)
                    axret[i] = axret[i] + (m[j]/(Rij**2))*((x[j]-x[i])/Rij)
                    ayret[i] = ayret[i] + (m[j]/(Rij**2))*((y[j]-y[i])/Rij)
        """
        xjg, xig = np.meshgrid(x, x)
        yjg, yig = np.meshgrid(y, y)
        mj, mi = np.meshgrid(m, m)
        R = ((xjg - xig)**2+(yjg-yig)**2)**(1/2) + 1e-3
        
        axret = (mj/(R**2))*((xjg-xig)/R)
        ayret = (mj/(R**2))*((yjg-yig)/R)
        np.fill_diagonal(axret, 0)
        np.fill_diagonal(ayret, 0)
        #print(axret.sum(axis=1))
        #print(ayret.sum(axis=1))
        axret = axret.sum(axis=1)
        ayret = ayret.sum(axis=1)
        #print(xig)
        #print(xjg)
        
        
        #print(vxret)
        #print(vyret)
        #print(axret)
        #print(ayret)
        #ret = np.concatenate((vxret,vyret,axret,ayret),axis=0)
        ret = np.vstack([m, vxret,vyret,axret,ayret]).T
        #print(ret)

            
        return ret.reshape(1,-1).squeeze()
    #print(init_data.reshape(1,-1).squeeze())
    sol = solve_ivp(f_particles, [0,1], init_data.reshape(1,-1).squeeze(), t_eval=[deltat], method='DOP853')
    #print(sol.y.reshape(-1,5))
    positions = sol.y.reshape(-1,5)[:,1:2+1]
    return positions

if __name__ == '__main__':
    deltat = 0.143235
    ret = multibody_positions(deltat)
    print(ret)
