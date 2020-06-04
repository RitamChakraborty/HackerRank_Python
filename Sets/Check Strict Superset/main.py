# https://www.hackerrank.com/challenges/py-check-strict-superset/problem


def check_strict_superset():
    super_set = set(input().strip().split())
    t = int(input())

    for _ in range(t):
        sub_set = set(input().strip().split())
        if super_set == super_set.union(sub_set) or len(super_set.difference(sub_set)) == 0:
            return False

    return True


if __name__ == '__main__':
    print(check_strict_superset())
