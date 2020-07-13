# https://www.hackerrank.com/challenges/zipped/problem

if __name__ == '__main__':
    s, n = map(int, input().strip().split())
    all_marks = []

    for _ in range(n):
        marks = list(map(float, input().strip().split()))
        all_marks.append(marks)

    zipped = zip(*all_marks)

    for lst in list(zipped):
        total = sum(lst)
        print(total / n)
