# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem


if __name__ == '__main__':
    input()
    set_ = set(map(int, input().strip().split()))
    n = int(input().strip())

    for i in range(n):
        input_lst = input().strip().split()
        input_ = input_lst[0]

        if input_ == 'pop':
            set_.pop()
        elif input_ == 'remove':
            i = int(input_lst[1])
            set_.remove(i)
        elif input_ == 'discard':
            i = int(input_lst[1])
            set_.discard(i)

    print(sum(set_))
