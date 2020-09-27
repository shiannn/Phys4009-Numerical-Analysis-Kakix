import random

stations = ["Taipei Zoo",
            "Muzha",
            "Wanfang Community",
            "Wanfang Hospital",
            "Xinhai",
            "Linguang",
            "Liuzhangli",
            "Technology Building",
            "Daan",
            "Zhongxiao Fuxing",
            "Nanjing Fuxing",
            "Zhongshan Junior High School",
            "Songshan Airport",
            "Dazhi",
            "Jiannan Rd.",
            "Xihu",
            "Gangqian",
            "Wende",
            "Neihu",
            "Dahu Park",
            "Huzhou",
            "Donghu",
            "Nangang Software Park",
            "Taipei Nangang Exhibition Center",
            "Xiangshan",
            "Taipei 101/World Trade Center",
            "Xinyi Anhe",
            "Daan",
            "Daan Park",
            "Dongmen",
            "C.K.S. Memorial Hall",
            "NTU Hospital",
            "Taipei Main Station",
            "Zhongshan",
            "Shuanglian",
            "Minquan W. Rd.",
            "Yuanshan",
            "Jiantan",
            "Shilin",
            "Zhishan",
            "Mingde",
            "Shipai",
            "Qilian",
            "Qiyan",
            "Beitou",
            "Xinbeitou",
            "Fuxinggang",
            "Zhongyi",
            "Guandu",
            "Zhuwei",
            "Hongshulin",
            "Tamsui",
            "Xindian",
            "Xindian District Office",
            "Qizhang",
            "Xiaobitan",
            "Dapinglin",
            "Jingmei",
            "Wanlong",
            "Gongguan",
            "Taipower Building",
            "Guting",
            "C.K.S. Memorial Hall",
            "Xiaonanmen",
            "Ximen",
            "Beimen",
            "Zhongshan",
            "Songjiang Nanjing",
            "Nanjing Fuxing",
            "Taipei Arena",
            "Nanjing Sanmin",
            "Songshan",
            "Nanshijiao",
            "Jingan",
            "Yongan Market",
            "Dingxi",
            "Guting",
            "Dongmen",
            "Zhongxiao Xinsheng",
            "Songjiang Nanjing",
            "Xingtian Temple ",
            "Zhongshan Elementary School",
            "Minquan W. Rd.",
            "Daqiaotou",
            "Taipei Bridge",
            "Cailiao",
            "Sanchong",
            "Xianse Temple",
            "Touqianzhuang",
            "Xinzhuang",
            "Fu Jen University",
            "Danfeng",
            "Huilong",
            "Sanchong Elementary School",
            "Sanhe Junior High School",
            "St. Ignatius High School",
            "Sanmin Senior High School",
            "Luzhou",
            "Dingpu",
            "Yongning",
            "Tucheng",
            "Haishan",
            "Far Eastern Hospital",
            "Fuzhong",
            "Banqiao",
            "Xinpu",
            "Jiangzicui",
            "Longshan Temple",
            "Ximen",
            "Taipei Main Station",
            "Shandao Temple",
            "Zhongxiao Xinsheng",
            "Zhongxiao Fuxing",
            "Zhongxiao Dunhua",
            "S.Y.S. Memorial Hall",
            "Taipei City Hall",
            "Yongchun",
            "Houshanpi",
            "Kunyang",
            "Nangang",
            "Taipei Nangang Exhibition Center"]

intervals = [["Tamsui", "Hongshulin", 175],
             ["Hongshulin", "Zhuwei", 136],
             ["Zhuwei", "Guandu", 145],
             ["Guandu", "Zhongyi", 78],
             ["Zhongyi", "Fuxinggang", 109],
             ["Fuxinggang", "Beitou", 145],
             ["Beitou", "Qiyan", 91],
             ["Qiyan", "Qilian", 73],
             ["Qilian", "Shipai", 100],
             ["Shipai", "Mingde", 61],
             ["Mingde", "Zhishan", 76],
             ["Zhishan", "Shilin", 91],
             ["Shilin", "Jiantan", 92],
             ["Jiantan", "Yuanshan", 109],
             ["Yuanshan", "Minquan W. Rd.", 90],
             ["Minquan W. Rd.", "Shuanglian", 57],
             ["Shuanglian", "Zhongshan", 58],
             ["Zhongshan", "Taipei Main Station", 65],
             ["Taipei Main Station", "NTU Hospital", 63],
             ["NTU Hospital", "C.K.S. Memorial Hall", 83],
             ["C.K.S. Memorial Hall", "Dongmen", 165],
             ["Dongmen", "Daan Park", 65],
             ["Daan Park", "Daan", 70],
             ["Daan", "Xinyi Anhe", 81],
             ["Xinyi Anhe", "Taipei 101/World Trade Center", 81],
             ["Taipei 101/World Trade Center", "Xiangshan", 93],
             ["Songshan", "Nanjing Sanmin", 138],
             ["Nanjing Sanmin", "Taipei Arena", 102],
             ["Taipei Arena", "Nanjing Fuxing", 84],
             ["Nanjing Fuxing", "Songjiang Nanjing", 92],
             ["Songjiang Nanjing", "Zhongshan", 106],
             ["Zhongshan", "Beimen", 114],
             ["Beimen", "Ximen", 75],
             ["Ximen", "Xiaonanmen", 81],
             ["Xiaonanmen", "C.K.S. Memorial Hall", 75],
             ["C.K.S. Memorial Hall", "Guting", 83],
             ["Guting", "Taipower Building", 88],
             ["Taipower Building", "Gongguan", 67],
             ["Gongguan", "Wanlong", 119],
             ["Wanlong", "Jingmei", 87],
             ["Jingmei", "Dapinglin", 89],
             ["Dapinglin", "Qizhang", 75],
             ["Qizhang", "Xindian District Office", 78],
             ["Xindian District Office", "Xindian", 111],
             ["Qizhang", "Xiaobitan", 203],
             ["Beitou", "Xinbeitou", 157],
             ["Taipei Nangang Exhibition Center", "Nangang", 114],
             ["Nangang", "Kunyang", 105],
             ["Kunyang", "Houshanpi", 99],
             ["Houshanpi", "Yongchun", 73],
             ["Yongchun", "Taipei City Hall", 82],
             ["Taipei City Hall", "S.Y.S. Memorial Hall", 72],
             ["S.Y.S. Memorial Hall", "Zhongxiao Dunhua", 67],
             ["Zhongxiao Dunhua", "Zhongxiao Fuxing", 63],
             ["Zhongxiao Fuxing", "Zhongxiao Xinsheng", 84],
             ["Zhongxiao Xinsheng", "Shandao Temple", 76],
             ["Shandao Temple", "Taipei Main Station", 64],
             ["Taipei Main Station", "Ximen", 132],
             ["Ximen", "Longshan Temple", 103],
             ["Longshan Temple", "Jiangzicui", 190],
             ["Jiangzicui", "Xinpu", 74],
             ["Xinpu", "Banqiao", 102],
             ["Banqiao", "Fuzhong", 89],
             ["Fuzhong", "Far Eastern Hospital", 92],
             ["Far Eastern Hospital", "Haishan", 142],
             ["Haishan", "Tucheng", 106],
             ["Tucheng", "Yongning", 95],
             ["Yongning", "Dingpu", 180],
             ["Taipei Nangang Exhibition Center", "Nangang Software Park", 78],
             ["Nangang Software Park", "Donghu", 85],
             ["Donghu", "Huzhou", 78],
             ["Huzhou", "Dahu Park", 121],
             ["Dahu Park", "Neihu", 71],
             ["Neihu", "Wende", 78],
             ["Wende", "Gangqian", 72],
             ["Gangqian", "Xihu", 65],
             ["Xihu", "Jiannan Rd.", 110],
             ["Jiannan Rd.", "Dazhi", 103],
             ["Dazhi", "Songshan Airport", 172],
             ["Songshan Airport", "Zhongshan Junior High School", 142],
             ["Zhongshan Junior High School", "Nanjing Fuxing", 66],
             ["Nanjing Fuxing", "Zhongxiao Fuxing", 86],
             ["Zhongxiao Fuxing", "Daan", 67],
             ["Daan", "Technology Building", 69],
             ["Technology Building", "Liuzhangli", 122],
             ["Liuzhangli", "Linguang", 72],
             ["Linguang", "Xinhai", 124],
             ["Xinhai", "Wanfang Hospital", 106],
             ["Wanfang Hospital", "Wanfang Community", 99],
             ["Wanfang Community", "Muzha", 47],
             ["Muzha", "Taipei Zoo", 67],
             ["Luzhou", "Sanmin Senior High School", 110],
             ["Sanmin Senior High School", "St. Ignatius High School", 87],
             ["St. Ignatius High School", "Sanhe Junior High School", 82],
             ["Sanhe Junior High School", "Sanchong Elementary School", 104],
             ["Sanchong Elementary School", "Daqiaotou", 148],
             ["Huilong", "Danfeng", 159],
             ["Danfeng", "Fu Jen University", 110],
             ["Fu Jen University", "Xinzhuang", 130],
             ["Xinzhuang", "Touqianzhuang", 93],
             ["Touqianzhuang", "Xianse Temple", 105],
             ["Xianse Temple", "Sanchong", 142],
             ["Sanchong", "Cailiao", 84],
             ["Cailiao", "Taipei Bridge", 93],
             ["Taipei Bridge", "Daqiaotou", 115],
             ["Daqiaotou", "Minquan W. Rd.", 75],
             ["Minquan W. Rd.", "Zhongshan Elementary School", 72],
             ["Zhongshan Elementary School", "Xingtian Temple ", 89],
             ["Xingtian Temple ", "Songjiang Nanjing", 75],
             ["Songjiang Nanjing", "Zhongxiao Xinsheng", 114],
             ["Zhongxiao Xinsheng", "Dongmen", 118],
             ["Dongmen", "Guting", 192],
             ["Guting", "Dingxi", 187],
             ["Dingxi", "Yongan Market", 100],
             ["Yongan Market", "Jingan", 88],
             ["Jingan", "Nanshijiao", 103]]

def shortest_driving_time(start, end):
    ### START YOUR CODE HERE ###
    import numpy as np
    def constructMatrix():
        #print(len(stations))
        vertexNum = len(stations)
        #Graph = [[0]*vertexNum]*vertexNum
        Graph = np.zeros((vertexNum, vertexNum))
        for edge in intervals:
            st = stations.index(edge[0])
            ed = stations.index(edge[1])
            length = edge[2]
            Graph[st][ed] = length
            Graph[ed][st] = length
        #num = np.nonzero(Graph)
        #print(len(intervals))
        #print(len(num[0]))
        return Graph

    def minDistance(distance, vis):
        mini = np.Inf
        mini_idx = -1
        for v in range(len(distance)):
            if distance[v] < mini and vis[v] == False:
                mini = distance[v]
                mini_idx = v
        return mini_idx

    Graph = constructMatrix()
    #print(Graph)
    
    distance = np.full(len(stations), np.Inf)
    st = stations.index(start)
    ed = stations.index(end)
    distance[st] = 0
    vis = [False]*len(stations)
    for _ in range(len(stations)):
        u = minDistance(distance, vis)
        vis[u] = True
        for v in range(len(stations)):
            if(vis[v]==False and (distance[u]+Graph[u][v] < distance[v])
            and Graph[u][v] > 0):
                distance[v] = distance[u] + Graph[u][v]
    #print(distance)
    dist = distance[ed]

    #### END YOUR CODE HERE ####
    return dist

if __name__ == '__main__':
    start, end = random.sample(stations, 2)
    #start, end = 'Tamsui', 'Zhuwei'
    #start, end = 'Beitou', 'Guting'
    #start, end = 'Fu Jen University', 'Tamsui'
    #start, end = 'Xindian District Office', 'Taipei Main Station'
    #start, end = 'Daan', 'Nanshijiao'
    #start, end = 'Technology Building', 'Zhuwei'
    
    print('Shortest driving time from',start,'station to',end,'station:')
    print(shortest_driving_time(start, end),'sec')
    exit(0)
