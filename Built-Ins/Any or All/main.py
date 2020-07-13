# https://www.hackerrank.com/challenges/any-or-all/problem

if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    _all = all(list(map(lambda x: x >= 0, lst)))
    _any = any(list(map(lambda x: str(x) == str(x)[::-1], lst)))

    if _all:
        print(_any)
    else:
        print(False)

# One liner solution
# print([all(list(map(lambda x: x >= 0, i))) and any(list(map(lambda x: str(x) == str(x)[::-1], i))) for i in [list(map(int, [input() for _ in range(2)][1].split()))]][0])
