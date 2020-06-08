# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
import collections

if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    default_dict = collections.defaultdict(list)

    for i in range(n):
        value = input().strip()
        default_dict[value].append(i + 1)

    for i in range(m):
        value = input().strip()
        if default_dict.keys().__contains__(value):
            print(" ".join(list(map(str, default_dict[value]))))
        else:
            print(-1)
