# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem


def average(array):
    set_ = set(array)
    return "{:.3f}".format(sum(set_) / len(set_))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
