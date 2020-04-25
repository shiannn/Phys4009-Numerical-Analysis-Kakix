import numpy as np

def central_cell_is_alive(p):
    decision = True
    sum8 = p[0:p.shape[0],0:p.shape[1]].sum() - p[p.shape[0]//2, p.shape[1]//2]
    sum8 = sum8.item()
    decision = (sum8==3)
    return decision

if __name__ == '__main__':
    p = np.array([[ 1,  0,  0 ],
       [ 1,  0,  0 ],
       [ 0,  1,  0 ]], dtype='int')
    
    ret = central_cell_is_alive(p)
    print(ret)