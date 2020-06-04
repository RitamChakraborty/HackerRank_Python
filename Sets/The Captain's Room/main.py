# https://www.hackerrank.com/challenges/py-the-captains-room/problem


if __name__ == '__main__':
    k = int(input().strip())
    lst = list(map(int, input().strip().split()))
    s = set(lst)

    print((sum(s) * k - sum(lst)) // (k - 1))
