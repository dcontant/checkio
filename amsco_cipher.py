from math import ceil
'''
The Amsco Cipher is a transpostion cipher. Choose a number of columns, then write the plaintext ( no whitespace) into the columns going from left to right, alternating between writing one or two plaintext letters into each adjacent column and rows . Number the columns with a key consisting of unique digit, then write the ciphertext by going down each numbered column in order. 

msg = 'lorem ipsum dolor sit amet',  key = 4123

4   1   2   3
l   or  e  mi
ps  u  md  o
l   or  s  it
am  e   t

encode text = oruoreemdstmioitlpslam

'''
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def encode_amsco(string, key):
    msg = ''.join([char for char in string if char.isalpha()])
    key = str(key)
    key_length = len(key)
    mean_row_length = (3 * key_length + 2)/2 - 1
    number_of_rows = ceil(len(msg)/mean_row_length)
    matrix = [['' for i in range(key_length)] for j in range(number_of_rows)]
    msg = iter(msg)
    for i in range(number_of_rows):
        for j in range(key_length):
            if i%2 != j%2:
                try:
                    temp = next(msg)
                    temp += next(msg)
                    matrix[i][j] = temp
                    temp = ''
                except StopIteration:
                    matrix[i][j] = temp
                    temp = ''
                    break
            else:
                try:
                    matrix[i][j] = next(msg)
                except StopIteration:
                    break
    encode_msg = ''
    matrix.insert(0,[n for n in key])
    for row in sorted(transpose(matrix)):
        encode_msg += ''.join(row[1:])
    return encode_msg
    
    
def decode_amsco(string, key):
    key = str(key)
    key_length = len(key)
    mean_row_length = (3* key_length + 2)/2 - 1
    number_of_rows = ceil(len(string)/mean_row_length)
    matrix = [[0 for i in range(key_length)] for j in range(number_of_rows)]
    sum_of_char = 0
    for i in range(number_of_rows):
        for j in range(key_length):
            if sum_of_char >= len(string):
                matrix[i][j] = 0
            elif sum_of_char == len(string)-1:
                matrix[i][j] = 1
            elif i%2 != j%2:
                matrix[i][j] = 2
            else:
                matrix[i][j] = 1
            sum_of_char += matrix[i][j]
    matrix.insert(0,[n for n in key])
    matrix = [row[1:] for row in sorted(transpose(matrix))]
    string = iter(string)
    for col in matrix:
        for j in range(number_of_rows):
            cell_value = col[j]
            col[j] = ''
            for k in range(cell_value):
                col[j] += next(string)
    temp = []
    for digit in key:
        temp.append(matrix[int(digit)-1])
    matrix = transpose(temp)
    decode_message = ''.join(''.join(col for col in row) for row in matrix)
    return decode_message
    
