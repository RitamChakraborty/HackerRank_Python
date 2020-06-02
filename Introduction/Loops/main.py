# https://www.hackerrank.com/challenges/python-loops/problem


if __name__ == '__main__':
    n = int(input())

    for i in map(lambda x: x**2, range(n)):
        print(int(i))
