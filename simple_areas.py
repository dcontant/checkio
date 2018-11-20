from math import sqrt, pi

def simple_areas(*args):

    def answer(n):
        if n - int(n) == 0:
            return int(n)
        else:
            return round(n, 2)

    def circle(args):
        d = args[0]
        return answer(pi * (d/2)**2)

    def square(args):
        w,l = args
        return answer(w * l)

    def triangle(args):
        a,b,c = args
        p = (a+b+c)/2
        return answer(sqrt(p * (p-a) * (p-b) * (p-c)))
    
    figures = {1: circle, 2: square, 3: triangle}

    return figures[len(args)](args)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"
    print('tests all passed')
