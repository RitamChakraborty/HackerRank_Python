# https://www.hackerrank.com/challenges/py-set-add/problem


if __name__ == '__main__':
    n = int(input().strip())
    set_ = set()

    for _ in range(n):
        input_ = input().strip()
        set_.add(input_)

    print(set_)
    print(len(set_))

# One liner
# print(len(set(input() for _ in range(int(input())))))
