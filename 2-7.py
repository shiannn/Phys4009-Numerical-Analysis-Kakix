def printChar():
    for i in range(65,65+26):
        line = ''
        for j in range(i,i+26):
            temp = 65+((j-65) % 26)
            #print(chr(temp))
            line += chr(temp)
        print(line)

if __name__ == '__main__':
    printChar()