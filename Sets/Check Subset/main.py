# https://www.hackerrank.com/challenges/py-check-subset/problem


if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        input()
        sub = set(input().strip().split())
        input()
        super = set(input().strip().split())
        print(super == super.union(sub))
