import re

if __name__ == '__main__':
    n = int(input())
    colors = []

    for _ in range(n):
        line = input()
        findall = re.findall(r"#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})[^\s]", line)
        for i in findall:
            print('#' + i)
