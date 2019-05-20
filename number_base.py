from string import ascii_uppercase, digits

def checkio(number, base):
    # convert a number to base 10, valid for base 2 to 36
    base_digits = dict(zip((digits + ascii_uppercase)[:base], range(base)))
    try:
        return sum(base_digits[digit]*base**(len(number)-i-1) for i,digit in enumerate(number))
    except KeyError:
        return -1
    
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("all good")
