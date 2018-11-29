def checkio(game_result):
    gr = game_result
    for row in gr:
        if row[0] == row[1] == row[2] != '.':
            return row[0]
    for col in zip(*gr):
        if col[0] == col[1] == col[2] != '.':
            return col[0]
    center = gr[1][1]
    if gr[2][0] == center == gr[0][2] != '.':
        return center
    if gr[0][0] ==  center == gr[2][2] != '.':
        return center
    return 'D'
    
    
if __name__ == '__main__':
    
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("all good")
