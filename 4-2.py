def rotate_characters(input):
    output = ''
    for a in input:
        temp = ord(a)+1
        if a == 'z' or a== 'Z':
            temp -= 26
        output += chr(temp)
    return output

if __name__ == '__main__':
    input = 'banana'
    ret = rotate_characters(input)
    print(ret)