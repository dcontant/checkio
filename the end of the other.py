from itertools import combinations as comb
def checkio(words_set):
    for c in comb(words_set,2):
        if c[0].endswith(c[1]) or c[1].endswith(c[0]):
            print(c)
            return True
    return False     

if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
    print('all good')
