def navigation(seaside):
    def distance(a,b):
        di = abs(a[0]-b[0])
        dj = abs(a[1]-b[1])
        diag = min(di,dj)
        straight = max(di,dj)-min(di,dj)
        return diag + straight
    
    for i,row in enumerate(seaside):
        for j, value in enumerate(row):
            if value == 'Y':
                y = (i,j)
            if value == 'C':
                c = (i,j)
            if value == 'M':
                m = (i,j)
            if value == 'S':
                s = (i,j)
    
    return distance(y,c) + distance(y,m) + distance(y,s)

if __name__ == '__main__':
    print("Example:")
    print(navigation([['Y', 0, 0, 0, 'C'],
                      [ 0,  0, 0, 0,  0],
                      [ 0,  0, 0, 0,  0],
                      ['M', 0, 0, 0, 'S']]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert navigation([['Y', 0, 0, 0, 'C'],
                       [ 0,  0, 0, 0,  0],
                       [ 0,  0, 0, 0,  0],
                       ['M', 0, 0, 0, 'S']]) == 11

    assert navigation([[ 0,  0, 'C'],
                       [ 0, 'S', 0],
                       ['M','Y', 0]]) == 4

    assert navigation([[ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'M', 0, 'S', 0],
                       [ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'C', 0,  0,  0],
                       [ 0, 'Y',0,  0,  0,  0,  0],
                       [ 0,  0, 0,  0,  0,  0,  0]]) == 9
    print("Coding complete? Click 'Check' to earn cool rewards!")
