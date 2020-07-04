''' 
Determine whether the sequence of elements items is ascending so that its each element is strictly 
larger than (and not merely equal to the element that precedes it.
'''

def is_ascending(items):
    if len(items)<2:
        return True
    else:
        curr1 = items[0]
        for i in range(1,len(items)):
            curr2 = items[i]
            if curr1 >= curr2:
                return False
            else:
                curr1 = curr2
    return True


if __name__ == '__main__':
    print("Example:")
    print(is_ascending([-5, 10, 99, 123456]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
