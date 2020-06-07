# https://www.hackerrank.com/challenges/polar-coordinates/problem
import cmath

if __name__ == '__main__':
    c = complex(input().strip())
    r, rho = cmath.polar(c)
    print(r)
    print(rho)
