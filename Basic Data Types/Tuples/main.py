# https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    t = tuple((i for i in integer_list))
    print(hash(t))


