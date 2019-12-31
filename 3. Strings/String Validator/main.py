# https://www.hackerrank.com/challenges/string-validators/problem


if __name__ == '__main__':
    s = input()
    lst = list(s)

    contains_alnum = False
    contains_alpha = False
    contains_digit = False
    contains_lower = False
    contains_upper = False

    for i in lst:
        s = str(i)

        if ~contains_alnum:
            if s.isalnum():
                contains_alnum = True
        if ~contains_alpha:
            if s.isalpha():
                contains_alpha = True
        if ~contains_digit:
            if s.isdigit():
                contains_digit = True
        if ~contains_lower:
            if s.islower():
                contains_lower = True
        if ~contains_upper:
            if s.isupper():
                contains_upper = True

    print(contains_alnum)
    print(contains_alpha)
    print(contains_digit)
    print(contains_lower)
    print(contains_upper)
