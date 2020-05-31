from itertools import permutations 
def bigger_together(numbers: int) -> int:
    numbers = [int(''.join(n)) for n in permutations(map(str,numbers))]
    return max(numbers)-min(numbers)
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert bigger_together([1,2,3,4]) == 3087, "4321 - 1234"
    assert bigger_together([1,2,3,4, 11, 12]) == 32099877, "43212111 - 11112234"
    assert bigger_together([0, 1]) == 9, "10 - 01"
    assert bigger_together([100]) == 0, "100 - 100"
    print('Done! I feel like you good enough to click Check')
    
