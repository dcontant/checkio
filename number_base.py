from string import ascii_uppercase, digits

def checkio(number, radix):
    possible = dict(zip(str(digits + ascii_uppercase)[:radix], range(radix)))
    if any(digit not in possible for digit in number):
        return -1
    return sum(possible[digit]*radix**(len(number)-i-1) for i,digit in enumerate(number))


#
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("all good")
