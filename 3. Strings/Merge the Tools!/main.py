# https://www.hackerrank.com/challenges/merge-the-tools/problem


def merge_the_tools(input, k):
    lst = []
    for i in range(len(input) // k):
        lst.append(input[i * k: (i + 1) * k])

    for i in lst:
        s = ''
        for j in i:
            if j not in s:
                s += j
        print(s)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
