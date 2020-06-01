# https://www.hackerrank.com/challenges/designer-door-mat/problem


def get_row(m, i):
    s = ".|." * (i * 2 + 1)
    ss = s.center(m, "-")
    return ss


def make_mat(n, m):
    for i in range(n // 2):
        print(get_row(m, i))

    w = "welcome".upper().center(m, "-")
    print(w)

    for i in reversed(range(n // 2)):
        print(get_row(m, i))


if __name__ == '__main__':
    i = input().split()
    N, M = int(i[0]), int(i[1])
    make_mat(N, M)
