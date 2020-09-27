import numpy as np
import matplotlib.pyplot as plt

def solve_maze(maze):
    ret = maze.copy()
    ### START YOUR CODE HERE ###
    import sys
    sys.setrecursionlimit(100000)
    direction = [[-1,0],[0,-1],[1,0],[0,1]]
    def dfs(st):
        print(st)
        if st[0] == 149 and st[1] == 150:
            return True
        for dire in direction:
            st[0] += dire[0]
            st[1] += dire[1]
            if ret[st[0]][st[1]] == 0 and not(st[0] < 0 or st[0] > 150 or st[1] < 0 or st[1] > 150):
                ret[st[0]][st[1]] = 1
                if(dfs(st)):
                    return True
                ret[st[0]][st[1]] = 0
            st[0] -= dire[0]
            st[1] -= dire[1]
        return False

    ret[1,0] = 1
    dfs([1,0])
    # dfs

    #### END YOUR CODE HERE ####
    return ret

if __name__ == '__main__':
    data = np.load('maze_data.npy')
    sol = np.load('maze_solve.npy')
    
    idx = np.random.randint(50)
    idx = 6
    ret = solve_maze(data[idx])
    #solve = sol[idx]
    #print((ret-solve).nonzero())
    
    fig = plt.figure(figsize=(6,6), dpi=80)
    plt.imshow(ret,cmap='Blues')
    plt.show()
