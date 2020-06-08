# https://www.hackerrank.com/challenges/piling-up/problem
import collections


def pile_up(d):
    while d:
        big = d.popleft() if d[0] > d[-1] else d.pop()

        if d:
            if d[-1] > big or d[0] > big:
                return False

    return True


if __name__ == '__main__':
    t = int(input())

    for t in range(t):
        input()
        dq = collections.deque(list(map(int, input().split())))

        if pile_up(dq):
            print("Yes")
        else:
            print("No")
