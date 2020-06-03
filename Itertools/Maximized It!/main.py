# https://www.hackerrank.com/challenges/maximize-it/problem
import itertools


def maximize(lst, m):
    print(max(sum(j ** 2 for j in i) % m for i in itertools.product(*lst)))


if __name__ == '__main__':
    ls = input().strip().split()
    K, M = int(ls[0]), int(ls[1])
    L = []

    for _ in range(K):
        ls = input().strip().split()
        n, LST = int(ls[0]), list(map(int, set(ls[1:])))
        L.append(LST)

    maximize(L, M)

# Short version

# k, m = map(int, input().split())
# print(max(sum(j ** 2 for j in i) % m for i in __import__('itertools').product(*[list(map(int, set(input().split()[1:]))) for _ in range(k)])))

# Spread out version
# (I'm a Flutter developer
# I'm used to looking at this kinda code)

# k, m = map(int, input().split())
# print(
#     max(
#         sum(
#             j ** 2 for j in i
#         ) % m for i in __import__('itertools').product(
#             *[
#                 list(
#                     map(
#                         int,
#                         set(
#                             input().split()[1:]
#                         )
#                     )
#                 ) for _ in range(k)
#             ]
#         )
#     )
# )
