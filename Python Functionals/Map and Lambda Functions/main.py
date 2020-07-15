cube = lambda x: x ** 3


def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        lst = [0, 1]
        a = 0
        b = 1

        for i in range(n - 2):
            c = a + b
            a = b
            b = c
            lst.append(c)

        return lst


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
