# https://www.hackerrank.com/challenges/collections-counter/problem
import collections

if __name__ == '__main__':
    earning = 0
    input()
    shoes = list(map(int, input().strip().split()))
    shoe_counter = collections.Counter(shoes)

    t = int(input().strip())

    for _ in range(t):
        shoe, amount = map(int, input().strip().split())

        if shoe_counter.keys().__contains__(shoe):
            if shoe_counter[shoe] > 0:
                shoe_counter[shoe] -= 1
                earning += amount

    print(earning)
