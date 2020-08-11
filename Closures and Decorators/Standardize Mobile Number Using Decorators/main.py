def wrapper(f):
    def fun(l):
        return f(list(map(lambda i: "+91" + " " + i[-10:len(i) - 5] + " " + i[-5:len(i)], l)))

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
