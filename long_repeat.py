def long_repeat(line):
    limit = len(line)
    ans = [0]
    for i in range(limit):
        char = line[i]
        current = 1
        for j in range(i+1,limit+1):
            if line[i:j] == char*(j-i):
                current = j-i
        ans.append(current)
    return max(ans)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
