# https://www.hackerrank.com/challenges/input/problem

if __name__ == '__main__':
    x, k = map(int, input().strip().split())
    ploy = input()
    poly_eval = eval(ploy)
    print(poly_eval == k)
