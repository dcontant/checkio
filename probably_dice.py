

from operator import mul

from functools import reduce


def probability(dices, sides, target):

    # the strategy is to first determined all possible partitions of the target in k-parts, k being the number of 

    # dices with values between 1 and the number of faces of each dices

    # for each partition, we must take into account that each dice can obtain the necessary value giving k! permu-

    # tations. If a value is not unique, this number must be divided by the r!, r being the number of repetitions for

    # each repeating value. The sum of all these possible correct result is divide by the total number of possibi-

    # lities to obtain the probability

    n = target

    k = dices

    a = 1

    b = sides

    

    def partitions(n, k, a, b):

        # partitions of natural number n in k parts with values between a <= n <= b

        min_x = max(a, n - (k-1) * b)

        max_x = min(b, n - (k-1) * a)

        if k == 1 and a <= n <= b:

            yield [n]

        elif n > 0 and k > 0:

            for x in range(min_x, max_x+1):

                for p in partitions(n-x, k-1, x, b):

                    yield [x] + p

                    

    def fac(n):

        # factorial of n

        ans = n

        while n > 1:

            ans *= n - 1

            n -= 1

        return ans

    

    

    return round(sum((fac(k)/reduce(mul, [fac(p.count(i)) for i in set(p)])) for p in partitions(n,k,a,b))/(b**k), 4)

