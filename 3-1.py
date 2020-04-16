import math
func = 0.
for m in range(1,3+1):
    for n in range(1,3+1):
        func += m*(math.pi)**n

func = math.log(func)
print('value:',func)