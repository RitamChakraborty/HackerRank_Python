import re

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        _input = input()
        _match = re.match(r"(\w+) <(.+)>", _input)
        name = _match.group(1)
        email = _match.group(2)

        _match = re.match(r"^[a-z][a-z0-9._\-]+@[a-z]+\.[a-z]{1,3}$", email)
        if _match:
            print(_input)
