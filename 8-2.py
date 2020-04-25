import numpy as np
from scipy.signal import convolve2d

pattern = \
np.array([[0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,1,1,1,0,0,0,0],
          [0,0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,1,1,1,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,1,1,1,0,0,0,0],
          [0,0,0,0,1,1,1,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,1,1,1,0,0,0,0],
          [0,0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,1,1,1,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0]], dtype='int')


def game_of_life(n):
    kernel = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])
    p = pattern.copy()
    for it in range(n):
        neighbor = convolve2d(p, kernel, mode='same')
        #print(np.logical_and(p == 1, neighbor<2))
        ### Any live cell with fewer than 2 live neighbours dies, as if caused by underpopulation.
        ### Any live cell with 2 or 3 live neighbours lives on to the next generation.
        ### Any live cell with more than 3 live neighbours dies, as if by overpopulation.
        ### Any dead cell with exactly 3 live neighbours becomes a live cell, as if by reproduction.

        #print(((p == 1) & ((neighbor<2) | (neighbor>3)))|((p==0)&(neighbor!=3)))
        condition = ((p == 1) & ((neighbor<2) | (neighbor>3) )) | ( (p==0) & (neighbor!=3) )
        ret = np.where(condition, np.zeros(p.shape), np.ones(p.shape))
        
        #print(ret)
        p = ret

    return p

if __name__ == '__main__':
    ret = game_of_life(10)
    print(ret)