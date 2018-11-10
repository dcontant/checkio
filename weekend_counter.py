from datetime import date, timedelta

def checkio(start,end):
    saturday, sunday = 5,6
    full_weeks = ( end - start ) // timedelta(7)
    start_day = start.weekday()
    end_day = end.weekday()
    if end_day < start_day:
        remaining_days =  (2 * int(start_day <= saturday)) + (1 * int(start_day == sunday))
    elif end_day == start_day:
        remaining_days = start_day in [saturday, sunday]
    else:
        remaining_days = int(end_day == saturday) + (2 * int(end_day == sunday))
    print(start_day, end_day,full_weeks, remaining_days)
    return full_weeks * 2 + remaining_days

if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"
    print('all good')
