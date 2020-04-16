def pronounce_the_number(N):
    number_in_text = ['zero',
    'one','two','three','four','five','six','seven','eight','nine','ten',
    'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen',
    'nineteen','twenty']

    return number_in_text[N]

if __name__ == '__main__':
    ret = pronounce_the_number(7)
    print(ret)