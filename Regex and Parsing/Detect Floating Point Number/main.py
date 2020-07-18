import re

if __name__ == '__main__':
    n = int(input())
    pattern = r"^(\+|\-)?\d*\.\d+$"

    for _ in range(n):
        _input = input()
        print(bool(re.fullmatch(pattern, _input)))
