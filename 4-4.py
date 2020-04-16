def insert_sum_between_two_digits(input):
    output = ''
    for i in range(4):
        temp = []
        for j in range(1,len(input)):
            temp.append(int(input[j])+int(input[j-1]))
        tempInput = ''
        for j in range(len(input)):
            if(j < len(input)):
                tempInput += input[j]
            if(j < len(temp)):
                tempInput += str(temp[j])
        print(tempInput)
        input = tempInput
    output = tempInput
    return output

if __name__ == '__main__':
    input = '12'
    ret = insert_sum_between_two_digits(input)
    print(ret)