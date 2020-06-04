# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem


if __name__ == '__main__':
    input()
    s1 = set(input().strip().split())
    input()
    s2 = set(input().strip().split())

    s3 = s1.intersection(s2)
    print(len(s3))
