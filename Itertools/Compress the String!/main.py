# https://www.hackerrank.com/challenges/compress-the-string/problem
import itertools


def compress(s):
    for i in itertools.groupby(s):
        print(tuple([len(list(i[1])), int(i[0])]), end=' ')


if __name__ == '__main__':
    string = input()
    compress(string)