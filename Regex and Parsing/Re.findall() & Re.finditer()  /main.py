import re

if __name__ == '__main__':
    _input = input()
    pattern = r"(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])"
    _finditer = re.findall(pattern, _input)

    if _finditer:
        for i in _finditer:
            print(i)
    else:
        print(-1)
