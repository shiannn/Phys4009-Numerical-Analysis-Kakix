import random

def password_generator():
    small = [chr(a) for a in range(97,97+26)]
    big = [chr(a) for a in range(65,65+26)]
    digit = [str(a) for a in range(10)]
    #print(small)
    #print(big)
    #print(digit)
    All = small + big + digit
    password = ""
    temp = random.sample(All,10)
    password = ''.join(temp)
    return password

if __name__ == '__main__':
    ret = password_generator()
    print(ret)