from typing import Iterable

def section_weight(section):
    total = 0
    length = len(section)
    for pos,weight in enumerate(section):
        total += (length-pos) * weight
    return total
        

def can_balance(weights: Iterable) -> int:
    total_length = len(weights)
    if total_length == 1:
        return 0
    for i in range(1,total_length-1):
        left_section = weights[:i]
        right_section = list(reversed(weights[i+1:]))
        if section_weight(left_section) == section_weight(right_section):
            return i
    return -1
    
    


if __name__ == '__main__':
    print("Example:")
    print(can_balance([6, 1, 10, 5, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert can_balance([6, 1, 10, 5, 4]) == 2
    assert can_balance([10, 3, 3, 2, 1]) == 1
    assert can_balance([7, 3, 4, 2, 9, 7, 4]) == -1
    assert can_balance([42]) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")

