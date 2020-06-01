# https://www.hackerrank.com/challenges/find-a-string/problem


def count_substring(string, sub_string):
    ln = len(string)
    i = 0
    c = 0

    while i < ln:
        ss = string[i:]
        f = ss.find(sub_string)

        if f == -1:
            break
        else:
            c += 1
            i = i + f + 1

    return c


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)