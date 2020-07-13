# https://www.hackerrank.com/challenges/python-sort-sort/problem

if __name__ == '__main__':
    n, m = map(int, input().split())
    athletes = []

    for _ in range(n):
        details = list(map(int, input().split()))
        athletes.append(details)

    k = int(input())

    sorted_athletes = sorted(athletes, key=lambda lst: lst[k])

    for i in sorted_athletes:
        print(" ".join(list(map(str, i))))
