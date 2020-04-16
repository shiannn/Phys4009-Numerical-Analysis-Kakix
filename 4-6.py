def prepare_n_to_mth_tuple(m,n):
    output = ()
    for i in range(1,n+1):
        output += (i**m,)
    return output

if __name__ == '__main__':
    m=3
    n=5
    ret = prepare_n_to_mth_tuple(m,n)
    print(ret)
