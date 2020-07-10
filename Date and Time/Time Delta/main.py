import datetime


def time_delta(date1, date2):
    ts1 = datetime.datetime.strptime(date1, '%a %d %b %Y %H:%M:%S %z').timestamp()
    ts2 = datetime.datetime.strptime(date2, '%a %d %b %Y %H:%M:%S %z').timestamp()

    return int(abs(ts1 - ts2))


if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        d1 = input().strip()
        d2 = input().strip()

        delta = time_delta(d1, d2)
        print(delta)
