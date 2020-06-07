# https://www.hackerrank.com/challenges/find-angle/problem
import math

if __name__ == '__main__':
    ab = int(input().strip())
    bc = int(input().strip())
    d = round(math.degrees(math.atan2(ab, bc)))
    print(str(d) + "°")
