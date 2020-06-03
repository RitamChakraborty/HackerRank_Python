# https://www.hackerrank.com/challenges/symmetric-difference/problem


def symmetric_difference(m, n):
    print("\n".join(map(str, sorted([i for i in m if i not in n] + [i for i in n if i not in m]))))


if __name__ == '__main__':
    input()
    m_ = set(map(int, input().split()))
    input()
    n_ = set(map(int, input().split()))
    symmetric_difference(m_, n_)

# Short version
# m, n = map(set, [map(int, input().strip().split()) for _ in range(4)][1:4:2])
# print("\n".join(map(str, sorted([i for i in m if i not in n] + [i for i in n if i not in m]))))
