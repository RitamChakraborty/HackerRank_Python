# https://www.hackerrank.com/challenges/py-collections-deque/problem
import collections

if __name__ == '__main__':
    d = collections.deque()
    n = int(input())

    for _ in range(n):
        inputs = input().split()
        operation = inputs[0]

        if operation == "append":
            value = int(inputs[1])
            d.append(value)
        elif operation == "appendleft":
            value = int(inputs[1])
            d.appendleft(value)
        elif operation == "pop":
            d.pop()
        elif operation == "popleft":
            d.popleft()

    print(" ".join(list(map(str, d))))
