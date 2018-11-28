'''
input: Unsanitized numeric or alphanumeric due to formatting purpose

output: List of its final character and sum of digits
'''

def checkio(data):
    data = ''.join(x for x in data if x.isalpha() or x.isdigit())[::-1]
    total = 0
    for i,d in enumerate(data):
        if i%2 == 0:
            d = 2 * (ord(d) - 48)
            if d >= 10:
                d = int(str(d)[0]) +  int(str(d)[1])
        else:
            d = ord(d) - 48
        total += d
    return [str((10 - total%10)%10), total]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio("799 273 9871") == ["3", 67]), "First Test"
    assert (checkio("139-MT") == ["8", 52]), "Second Test"
    assert (checkio("123") == ["0", 10]), "Test for zero"
    assert (checkio("999_999") == ["6", 54]), "Third Test"
    assert (checkio("+61 820 9231 55") == ["3", 37]), "Fourth Test"
    assert (checkio("VQ/WEWF/NY/8U") == ["9", 201]), "Fifth Test"

    print("OK, done!")
 
