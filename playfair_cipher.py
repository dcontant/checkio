from string import ascii_lowercase, digits

def encode(message, key_word):
    
    def key_table(key_word):
        ''' generate the 6x6 table with the key_word'''
        # remove duplicate in key_word
        temp = set()
        clean_kw = ''
        for x in key_word:
            if x not in temp:
                clean_kw += x
                temp.add(x)

        # generate key by combining key_word with letters+digits without duplicates
        key = clean_kw + ascii_lowercase + digits
        temp = set()
        final_key = ''
        for x in key:
            if x not in temp:
                final_key += x
                temp.add(x)

        # generate 6x6 table
        table = [['!' for i in range(6)] for j in range(6)]
        key_gen = iter(final_key)
        for i in range(6):
            for j in range(6):
                table[i][j] = next(key_gen)
        return table

    def digraphs(message):
        # formatted message in digraphs according to Playfair cipher rules
        clean_message = ''
        for x in message.lower():
            if x in ascii_lowercase + digits:
                clean_message += x
        while True:
            done = False
            for i in range(0,len(clean_message),2):
                if done:
                    break
                try:
                    a,b = clean_message[i],clean_message[i+1]
                    if a == b == 'x':
                        clean_message = clean_message[:i] + a + 'z' + clean_message[i+1:]
                        break
                    elif a == b:
                        clean_message = clean_message[:i] + a + 'x' + clean_message[i+1:]
                        break
                    elif len(clean_message) == 2:
                        done = True
                except IndexError:
                    if clean_message[-1] == 'z':
                        clean_message += 'x'
                        done = True
                    else:
                        clean_message += 'z'
                        done = True
                if i == len(clean_message)-2:
                    done = True
            if done: 
                break
        return [clean_message[i:i+2] for i in range(0,len(clean_message),2)]
    
    def coord(char, table):
        # find the coordinates of char in table
        for i,row in enumerate(table):
            if char in row:
                return (i, row.index(char))
    
    dig = digraphs(message)
    table = key_table(key_word)
    ciphertext = ''
        
    for d in dig:
        a,b = coord(d[0],table),coord(d[1],table)
        if a[0] == b[0]:
            aa = table[a[0]][(a[1]+1)%6]
            bb = table[a[0]][(b[1]+1)%6]
        elif a[1] == b[1]:
            aa = table[(a[0]+1)%6][a[1]]
            bb = table[(b[0]+1)%6][a[1]]
        else:
            aa = table[a[0]][b[1]]
            bb = table[b[0]][a[1]]
        ciphertext += ''.join((aa,bb))
    return ciphertext
    
    
    
def decode(message, key_word):
    # decode Playfair ciphertext
    
    def key_table(key_word):
        ''' generate the 6x6 table with the key_word'''
        # remove duplicate in key_word
        temp = set()
        clean_kw = ''
        for x in key_word:
            if x not in temp:
                clean_kw += x
                temp.add(x)

        # generate key by combining key_word with letters+digits without duplicates
        key = clean_kw + ascii_lowercase + digits
        temp = set()
        final_key = ''
        for x in key:
            if x not in temp:
                final_key += x
                temp.add(x)

        # generate 6x6 table
        table = [['!' for i in range(6)] for j in range(6)]
        key_gen = iter(final_key)
        for i in range(6):
            for j in range(6):
                table[i][j] = next(key_gen)
        return table
    
    def coord(char, table):
        # find the coordinates of char in table
        for i,row in enumerate(table):
            if char in row:
                return (i, row.index(char))
    
    dig = [message[i:i+2] for i in range(0,len(message),2)]
    table = key_table(key_word)
    plaintext = ''

    for d in dig:
        a,b = coord(d[0],table),coord(d[1],table)
        if a[0] == b[0]:
            aa = table[a[0]][(a[1]-1)%6]
            bb = table[a[0]][(b[1]-1)%6]
        elif a[1] == b[1]:
            aa = table[(a[0]-1)%6][a[1]]
            bb = table[(b[0]-1)%6][a[1]]
        else:
            aa = table[a[0]][b[1]]
            bb = table[b[0]][a[1]]
        plaintext += ''.join((aa,bb))
    return plaintext


assert encode("Fizz Buzz is x89 XX.", "checkio101") == 'do2y7mt22kry94y2y2', "Encode fizz buzz"
assert decode("do2y7mt22kry94y2y2", "checkio101") == 'fizxzbuzzisx89xzxz', "Decode fizz buzz"
assert encode("How are you?", "hello") == 'ea2imb1ht0', "Encode How are you"
assert decode("ea2imb1ht0", "hello") == 'howareyouz', "Decode How are you"
assert encode("My name is Alex!!!", "alexander") == 'i1dlkxjqlexn', "Encode Alex"
assert decode("i1dlkxjqlexn", "alexander") == 'mynameisalex', "Decode Alex"
assert encode("Who are you?", "human") == 'rnvftc1jd5', "Encode WHo"
assert decode("rnvftc1jd5", "human") == 'whoareyouz', "Decode Who"
assert encode("ATTACK AT DAWN", "general") == 'ewwektewhnua', "Encode attack"
assert decode("ewwektewhnua", "general") == 'attackatdawn', "Decode attack"
print('pass for all tests')
