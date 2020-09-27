import numpy as np
import matplotlib.pyplot as plt

def solve_puzzle(img):
    ret = img.copy()
    ### START YOUR CODE HERE ###
    edge = 120
    A = np.zeros((9,edge,edge,3),np.uint32)
    for i in range(9):
        m = i % 3
        n = i // 3
        A[i] = ret[m*edge:(m+1)*edge, n*edge:(n+1)*edge, :].copy()
    #plt.imshow(ret[m*edge:(m+1)*edge, n*edge:(n+1)*edge, :])
    #All permutation
    position = [0]*9
    vis = [0]*9
    Correct = np.zeros((3*edge,3*edge,3),np.uint32)


    maxdiffer = np.Inf

    def calMargin(img):
        diff = np.sum(np.square(img[:,120] - img[:,119]))+np.sum(np.square(img[:,240] - img[:,239]))
        diff += np.sum(np.square(img[120,:] - img[119,:]))+np.sum(np.square(img[240,:] - img[239,:]))
        return diff

    def dfs(idx):
        nonlocal ret
        if idx == 9:
            print(position)
            for cnt, a in enumerate(position):
                m = cnt % 3
                n = cnt // 3
                print(m,n)
                Correct[m*edge:(m+1)*edge, n*edge:(n+1)*edge, :] = A[a].copy()
            temp = calMargin(Correct)
            nonlocal maxdiffer
            if temp < maxdiffer:
                maxdiffer = temp
                ret = Correct.copy()
                #plt.imshow(ret)
                #plt.show()
            return

        for i in range(9):
            if vis[i] == 0:
                position[idx] = i
                vis[i] = 1
                dfs(idx+1)
                vis[i] = 0
    dfs(0)

    
    
    #### END YOUR CODE HERE ####
    return ret

if __name__ == '__main__':
    data = np.load('jigsaw_data.npy')
    
    idx = np.random.randint(10)
    idx = 0
    ret = solve_puzzle(data[idx])
    
    fig = plt.figure(figsize=(6,6), dpi=80)
    plt.imshow(ret)
    plt.show()