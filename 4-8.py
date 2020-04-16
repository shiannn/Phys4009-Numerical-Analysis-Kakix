def isFullHouse(cards):
    flag = None
    colors = []
    nums = []
    for card in cards:
        A = card.split('-')
        #print(A)
        colors.append(A[0])
        nums.append(A[1])
    Set = list(set(nums))
    if len(Set) != 2:
        return False
    else:
        if nums.count(Set[0])==2 and nums.count(Set[1])==3:
            return True
        elif nums.count(Set[0])==3 and nums.count(Set[1])==2:
            return True
        else:
            return False

if __name__=='__main__':
    cards = ['CLUB-7', 'DIAMOND-7', 'SPADE-7','DIAMOND-Q', 'CLUB-Q']
    ret = isFullHouse(cards)
    print(ret)
