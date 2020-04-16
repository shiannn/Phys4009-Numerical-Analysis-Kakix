def prepare_poker_deck():
    deck = []
    color = ['CLUB','DIAMOND','HEART','SPADE']
    number = ['A']+[str(a) for a in range(2,10+1)]+['J','Q','K']
    #print(number)
    for c in color:
        for n in number:
            deck.append(c+'-'+n)
    return deck

if __name__ == '__main__':
    ret = prepare_poker_deck()
    print(ret)