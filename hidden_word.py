def checkio(text, word):
    
    def transpose(matrix):
        return [list(row) for row in zip(*matrix)]
    
    def horizontal(text, word):
        for row,line in enumerate(text.lower().replace(' ', '').split('\n')):
            if word in line:
                col = line.find(word)
                return [row+1,col+1,row+1, col+len(word)]
        return False
    
    def vertical(text, word):
        text2 = text.lower().replace(' ', '').split('\n')
        dim = max(len(line) for line in text2)
        matrix = [[char for char in line  + '+' * (dim-len(line))] for line in text2]
        for col,line in enumerate(transpose(matrix)):
            line = ''.join(line)
            if word in line:
                row = line.find(word)+1
                return [row ,col+1, row+len(word)-1 , col+1]
        return False
    
    h = horizontal(text, word)
    v = vertical(text, word)
    
    if h:
        return h
    else:
        return v
    
    


if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
