# https://www.hackerrank.com/challenges/no-idea/problem


def count_happiness(n, m, lst, a, b):
    c = 0

    for i in lst:
        if i in a:
            c += 1
        elif i in b:
            c -= 1

    return c


if __name__ == '__main__':
    n_, m_ = map(int, input().split())
    lst_ = list(map(int, input().split()))
    a_ = set(map(int, input().split()))
    b_ = set(map(int, input().split()))

    happiness = count_happiness(n_, m_, lst_, a_, b_)
    print(happiness)
