import re

if __name__ == '__main__':
    n = int(input())
    pattern = r"^[789](\d){9}$"

    for _ in range(n):
        ph_no = input()
        match = re.match(pattern, ph_no)

        if match:
            print("YES")
        else:
            print("NO")
