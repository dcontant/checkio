'''
 A cipher grille is a 4×4 square of paper with four windows cut out. Placing the grille on a paper sheet of the same size, 
 the encoder writes down the first four symbols of his password inside the windows (see fig. below). After that, the encoder 
 turns the grille 90 degrees clockwise. The symbols written earlier become hidden under the grille and clean paper appears 
 inside the windows. The encoder then writes down the next four symbols of the password in the windows and turns the grille 
 90 degrees again. Then, they write down the following four symbols and turns the grille once more. Lastly, they write down 
 the final four symbols of the password. 
 '''
 def rot_90_clockwise(matrix):
    return [list(row) for row in zip(*reversed(matrix))]

def recall_password(cipher_grille, ciphered_password):
    ans = ''
    for _ in range(4):
        for i,row in enumerate(cipher_grille):
            for j,token in enumerate(row):
                if token == 'X':
                    ans += ciphered_password[i][j]
        cipher_grille = rot_90_clockwise(cipher_grille)
    return ans


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
    
    assert recall_password(
        ["....",
         "X..X",
         "X..X",
         "...."],
        ["cree",
         "band",
         "test",
         "yepp"]) == "bdttreepbdttreep"
    
    print('good for all tests')
