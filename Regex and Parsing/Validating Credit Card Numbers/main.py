# https://www.hackerrank.com/challenges/validating-credit-card-number/problem
import re

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        num = input()
        match = re.match(r"^(?!(?:.*(\d)(-?\1){3,}.*))[4-6]\d{3}((-\d{4}){3}|(\d{4}){3})$", num)

        if match:
            print("Valid")
        else:
            print("Invalid")
