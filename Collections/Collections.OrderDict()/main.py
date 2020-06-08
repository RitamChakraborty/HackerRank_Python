# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
import collections

if __name__ == '__main__':
    n = int(input().strip())
    order_dict = collections.OrderedDict()

    for _ in range(n):
        inputs = input().split()
        item_name = inputs[0]
        net_price = int(inputs[len(inputs) - 1])

        if len(inputs) == 3:
            item_name += " " + inputs[1]

        if order_dict.__contains__(item_name):
            order_dict[item_name] += net_price
        else:
            order_dict[item_name] = net_price

    for key, value in order_dict.items():
        print(key, value)
