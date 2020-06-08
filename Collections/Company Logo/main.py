# https://www.hackerrank.com/challenges/most-commons/problem

if __name__ == '__main__':
    name = input()
    d = dict()

    for i in name:
        if d.__contains__(i):
            d[i] += 1
        else:
            d[i] = 1

    lst = sorted(d.items(), key=lambda kv: kv[0])
    lst = sorted(lst, key=lambda kv: kv[1], reverse=True)

    for i in lst[:3]:
        print(i[0], i[1])
