def checkio(data):
    '''
    Given a list of numbers, you should find the sum of these numbers. 
    Your solution should not contain any of the banned words, even as a part of another word.

    The list of banned words are as follows:

        sum
        import
        for
        while
        reduce

    Input: A list of numbers.

    Output: The sum of numbers. 
    '''
    try:
        last = data.pop() 
        return checkio(data) + last
    except IndexError:
        return 0
