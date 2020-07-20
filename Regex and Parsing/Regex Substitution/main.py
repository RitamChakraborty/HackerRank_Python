import re

if __name__ == '__main__':
    code = "\n".join([input() for _ in range(int(input()))])
    code = re.sub(r"(?<= )\|\|(?= )", "or", code)
    code = re.sub(r"(?<= )&&(?= )", "and", code)

    print(code)
