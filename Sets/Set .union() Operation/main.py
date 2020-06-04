# https://www.hackerrank.com/challenges/py-set-union/problem


if __name__ == '__main__':
    s1, s2 = map(set, [i.split() for i in [input().strip() for _ in range(4)][1::2]])
    print(len(s1.union(s2)))

    # One liner solution
    # print(len(set(([input().strip() for _ in range(2)][1]).split()).union(set(([input().strip() for _ in range(2)][1]).split()))))
