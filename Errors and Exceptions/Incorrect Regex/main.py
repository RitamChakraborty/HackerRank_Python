import re

if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        pattern = input().strip()

        try:
            re.compile(pattern)
            print(True)
        except re.error as e:
            print(False)
