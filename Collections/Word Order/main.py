# https://www.hackerrank.com/challenges/word-order/problem
import collections

if __name__ == '__main__':
    n = int(input())
    order_dict = collections.OrderedDict()

    for _ in range(n):
        word = input()

        if order_dict.__contains__(word):
            order_dict[word] += 1
        else:
            order_dict[word] = 1

    print(len(order_dict.keys()))
    print(" ".join(list(map(str, order_dict.values()))))
