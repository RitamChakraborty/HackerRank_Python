import calendar

if __name__ == '__main__':
    inputs = list(map(int, input().strip().split()))
    month = inputs[0]
    day = inputs[1]
    year = inputs[2]

    cal = calendar.weekday(year=year, month=month, day=day)
    week_day = calendar.day_name[cal]
    print(week_day.upper())
