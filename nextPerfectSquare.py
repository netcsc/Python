'''
findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect
'''
def find_next_square(sq):
    if int(sq ** 0.5)**2 == sq:
        return int(sq ** 0.5 + 1)**2
    else:
        return -1
