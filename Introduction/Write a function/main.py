# https://www.hackerrank.com/challenges/write-a-function/problem
import calendar


def is_leap(y):
    return calendar.isleap(y)


year = int(input())
print(is_leap(year))
