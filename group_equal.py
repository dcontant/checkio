def group_equal(els):
    if not els:
        return []
    ans = []
    els = iter(els)
    current = [next(els)]
    while True:
        try:
            temp = next(els)
            if temp in current:
                current.append(temp)
            else:
                ans.append(current)
                current = [temp]
        except StopIteration:
            ans.append(current)
            break
    return ans


if __name__ == '__main__':
    print("Example:")
    print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [[1,1],[4,4,4],["hello","hello"],[4]]
    assert group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
    assert group_equal([1]) == [[1]]
    assert group_equal([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
