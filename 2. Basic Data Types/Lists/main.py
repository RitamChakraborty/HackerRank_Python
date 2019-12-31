# https://www.hackerrank.com/challenges/python-lists/problem


def main(n):
    lst = []

    for i in range(n):
        input_str = input()
        input_str_lst = input_str.split(" ")

        opt = input_str_lst[0]

        if opt == 'insert':
            pos = int(input_str_lst[1])
            num = int(input_str_lst[2])
            lst.insert(pos, num)
        if opt == 'remove':
            num = int(input_str_lst[1])
            lst.remove(num)
        if opt == 'append':
            num = int(input_str_lst[1])
            lst.append(num)
        if opt == 'sort':
            lst.sort()
        if opt == 'pop':
            lst.pop()
        if opt == 'reverse':
            lst.reverse()
        if opt == 'print':
            print(lst)


if __name__ == '__main__':
    N = int(input())

    main(N)
