

def n_bottles(num):
    '''
    '''
    return [str(n) + " bottles of beer on the wall" for n in range(num)]


def gemetria(word):
    ''' return the gematric value of word
    '''
    dict = {'א':1}


assert gemetria("abc") == 6
print("OK")
