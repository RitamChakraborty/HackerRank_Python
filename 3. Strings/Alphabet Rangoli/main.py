# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?h_r=next-challenge&h_v=zen


def print_rangoli(size):
    length = size * 4 - 3
    lst = []

    for i in range(size).__reversed__():
        s = ""

        for j in range(i, size).__reversed__():
            s += chr(97 + j) + "-"

        s = s[0:len(s) - 1]

        for j in range(i + 1, size):
            s += "-" + chr(97 + j)

        lst.append(s.center(length, '-'))

    lst += lst[0:len(lst) - 1].__reversed__()

    for i in lst:
        print(i)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)