def cut_sentence(line, length):
    if len(line) <=  length:
        return line
    left = line[:length]
    right = line[length:]
    if left[-1].isalpha() and right[0].isalpha():
        return ' '.join(left.split()[:-1])+'...'
    else:
        return ' '.join(left.split())+'...'
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert cut_sentence("Hi my name is Alex", 4) == "Hi...", "First"
    assert cut_sentence("Hi my name is Alex", 8) == "Hi my...", "Second"
    assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex", "Third"
    assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex", "Fourth"
    assert cut_sentence("Hi my name is Alex",9) == "Hi my..."
    assert cut_sentence("Hi my name is Alex",11) == "Hi my name..."

    print('Done! Do you like it? Go Check it!')
