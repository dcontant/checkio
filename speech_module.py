def checkio(number):

    FIRST_TWENTY = dict(zip(range(20),['', "one", "two", "three", "four", "five", "six", "seven","eight", "nine",
                                       "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen","sixteen", 
                                       "seventeen","eighteen", "nineteen"]))

    TENS = dict(zip(range(10) ,['','', "twenty", "thirty", "forty", "fifty", "sixty", "seventy","eighty", "ninety"]))

    hundreds = number//100
    number = number%100
    tens = number//10
    digits = number%10
    if tens < 2:
        digits += tens *10
        tens = 0
    
    return FIRST_TWENTY[hundreds] + ' hundred' * bool(hundreds) + ' ' * (bool(tens) and bool(hundreds)) \
            + TENS[tens]  +' ' * ((bool(tens) or bool(hundreds)) and bool(digits)) + FIRST_TWENTY[digits]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
