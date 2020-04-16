source = '''
Name    HW#1  HW#2  HW#3  HW#4  Midterm  FinalExam
James   10     6     8    10     90       86
Mary     9     8     9     9     78       80
Keith    7     7     8     7     92       82
Bruce    9     6     9    10     85       88
Kim      7     6     9     8     64       72
Emma    10     9     7     6     95       85
Cathy    6     7     7    10     73       77'''

def detect(x):
    if x != '':
        return 1
    else:
        return 0
### START YOUR CODE BELOW ###
print('Name    Average')
sep_list = source.split(sep="\n")
for i in range(2,len(sep_list)):
    #print(sep_list[i])
    name_Score = sep_list[i].split(sep=' ')
    #print(name_Score)
    name_Score = list(filter(detect, name_Score))
    total = 0
    for i in range(1,4+1):
        total += int(name_Score[i])
    for i in range(5,6+1):
        total += 0.3*int(name_Score[i])
    print(name_Score[0],' ',round(total))
