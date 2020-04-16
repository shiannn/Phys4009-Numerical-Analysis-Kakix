def find_least_common_multiple(M,N):
    tempMax = max(M,N)
    tempMin = min(M,N)
    least_common_multiple = tempMax
    while(least_common_multiple % tempMin != 0):
        #print(least_common_multiple)
        least_common_multiple += tempMax
    return least_common_multiple


if __name__ == '__main__':
    M = 17
    N = 31
    ret = find_least_common_multiple(M,N)
    print(ret)