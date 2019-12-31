# https://www.hackerrank.com/challenges/python-string-formatting/problem


def print_formatted(number):
    max_len = len(str(bin(number)).replace("0b", ""))
    s = ""

    for i in range(1, number + 1):
        s += str(i).rjust(max_len, " ") + " " \
            + str(oct(i)).replace("0o", "").rjust(max_len, " ") + " " \
            + str(hex(i)).replace("0x", "").upper().rjust(max_len, " ") + " " \
            + str(bin(i)).replace("0b", "").rjust(max_len, " ")
        s += "\n"

    print(s)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
