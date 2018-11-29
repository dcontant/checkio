'''
A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall. With this strategy, 
one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square. We have several white pawns 
on the chess board and only white pawns. You should design your code to find how many pawns are safe.

You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer. 
'''

def safe_pawns(pawns):
    col_dict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    pawns = [(int(p[1])-1,col_dict[p[0]]) for p in pawns] 
    board = [[0 for i in range(8)] for j in range(8)]
    for p in pawns:
        board[p[0]][p[1]] = 1
    safe = 0
    for row,col in pawns:
        if row > 0 and 0 < col < 7 :
            if board[row-1][col-1] or board[row-1][col+1]:
                safe += 1
        elif col == 0:
            if board[row-1][col+1]:
                safe += 1
        elif col == 7:
            if board[row-1][col-1]:
                safe += 1        
    return safe



if __name__ == '__main__':
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("all good")
