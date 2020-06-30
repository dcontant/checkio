def scan_board(start):
    ''' return all legal knight moves from a start cell'''
    col,row = start
    possibles_cells = []
    for col_delta in range(-2,3):
        for row_delta in range(-2,3):
            if sum((col_delta,row_delta))%2 and row_delta!=0 and col_delta!=0 :
                new_col = col + col_delta
                new_row = row + row_delta
                if 1 <= new_col <= 8 and 1 <= new_row <= 8:
                    possibles_cells.append((new_col, new_row))
    return set(possibles_cells)

def reformat(cells):
    ''' format cells as col= a to h, row= 1 to 8'''
    temp = []
    for c in cells:
        temp.append(chr(96+c[0])+str(c[1]))
    return sorted(temp)

def chess_knight(start, moves):
    possibles_cells = set()
    col, row = ord(start[0])-96 ,int(start[1]) # convert col and row to integer 1 to 8
    possibles_cells |= scan_board((col, row))
    if moves == 2:
        temp = set()
        for pc in possibles_cells:
            temp |= scan_board(pc)
        possibles_cells |= temp
    return reformat(possibles_cells)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert chess_knight('a1', 1) == ['b3', 'c2']
    assert chess_knight('h8', 2) == ['d6', 'd8', 'e5', 'e7', 'f4', 'f7', 'f8', 'g5', 'g6', 'h4', 'h6', 'h8']
