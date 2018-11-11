def checkio(n):
    def triangular(n):
        return n*(n+1)//2
    
    i = 1
    ans = 0
    while True:
        ans += i
        current = triangular(i)
        n -= current
        if n-current <= 0:
            break
        elif n/2 <= current <= n and n < triangular(i+1):
            ans += n-current
            break
        i +=1
    return ans

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
    assert checkio(3) == 2
    assert checkio(40) == 15 
    print('passed all tests ')
