# https://www.hackerrank.com/challenges/py-if-else/problem


def weird_detector(n):
    if n in range(6, 21) or n % 2 != 0:
        print('Weird')
    else:
        print('Not Weird')


if __name__ == '__main__':
    N = int(input().strip())
    weird_detector(N)
