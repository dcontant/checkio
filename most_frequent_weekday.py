'''
 You are given a year as integer (e. g. 2001). You should return the most frequent day(s) of the week in that year. 
 The result has to be a list of days sorted by the order of days in week (e. g. ['Monday', 'Tuesday']). Week starts with 
 Monday.

Input: Year as an int.

Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday). 
'''

from datetime import date
from collections import Counter

def most_frequent_days(year):
    weekdays = Counter()
    days_lookup = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
    for month in range(1,13):
        for day in range(1,32):
            try:
                weekdays.update([date(year,month,day).weekday()])
            except ValueError:
                pass
    max_n_of_days = weekdays.most_common(1)[0][1]
    answer = sorted([day[0] for day in weekdays.most_common() if day[1]== max_n_of_days])
    answer = [days_lookup[day] for day in answer]
    return answer

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
    assert most_frequent_days(328) == ["Monday","Sunday"]
    assert most_frequent_days(212) == ["Wednesday","Thursday"]
    print('all good')
