def encode(message, secret_alphabet, keyword):
    # ADFGVX cipher
    def clean_key(key_raw):
        key_clean = ''
        for char in key_raw:
            if char not in key_clean:
                key_clean += char
        return key_clean 
    
    def transpose(matrix):
        return [list(row) for row in zip(*matrix)]
    
    # cleaned keyword and message
    keyword = clean_key(keyword)
    message = ''.join(char.casefold() for char in message if char.isalnum())
    
    # build the fractionated form with the adfgvx table
    adfgvx = {0:'A',1:'D',2:'F',3:'G',4:'V',5:'X'}
    fractionated = ''
    for char in message:
        index = secret_alphabet.find(char)
        row = index//6
        col = index%6
        fractionated += adfgvx[row] + adfgvx[col]
        
    # build the transposed form with the fractionated form
    temp = []
    row_length = len(keyword)
    for i in range(0,len(fractionated),row_length):
        temp.append([char for char in fractionated[i:i+row_length]])
    temp[-1] += [''] * (row_length - len(temp[-1])) # padded last row with empty space
    temp = transpose(temp)
    transposed = dict(zip(keyword,temp))
    encode_message = ''
    for char in sorted(keyword):
        encode_message += ''.join(char for char in transposed[char] if char.isalpha())
    return encode_message

def decode(message, secret_alphabet, keyword):
    # ADFGVX cipher
    def clean_key(key_raw):
            key_clean = ''
            for char in key_raw:
                if char not in key_clean:
                    key_clean += char
            return key_clean 

    def transpose(matrix):
        return [list(row) for row in zip(*matrix)]

    keyword = clean_key(keyword)
    
    # dictionnary of columns length with cipher char as keys
    row_length = len(keyword)
    max_col_length = int(len(message)/row_length)+1
    last_row_length = len(message)%row_length
    col_length = dict(zip(keyword, [max_col_length if i < last_row_length else max_col_length-1 
                                    for i in range(row_length) ]))
    
    # build the transposed form
    transposition_table = dict()
    message = iter(message)
    temp = []
    for char in sorted(keyword):
        temp = [next(message) for _ in range(col_length[char])]
        if len(temp) < max_col_length:
            temp += [''] 
        transposition_table[char] = temp
    transposition_table = transpose([transposition_table[char] for char in keyword])
    
    # build the fractionated form with the transposed form
    adfgvx = {'A':0,'D':1,'F':2,'G':3,'V':4,'X':5}
    fractionated = ''.join([''.join(row) for row in transposition_table ])
    decode_message = ''
    for i in range(0,len(fractionated),2):
        index = adfgvx[fractionated[i]]*6 + adfgvx[fractionated[i+1]]
        decode_message += secret_alphabet[index]
    return decode_message


if __name__ == '__main__':
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
    assert decode("FXGAFVXXAXDDDXGA",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'iamgoing', "decode I am going"
    assert encode("attack at 12:00 am",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'attackat1200am', "decode attack"
    assert encode("ditiszeergeheim",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
    assert decode("DXGAXAAXXVDDFGFX",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'iamgoing', "decode weasel == weasl"
    print('all tests good')
