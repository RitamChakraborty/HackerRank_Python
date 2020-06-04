# https://www.hackerrank.com/challenges/py-set-mutations/problem


if __name__ == '__main__':
    input()
    set_ = set(input().strip().split())
    t = int(input().strip())

    for i in range(t):
        input_lst = input().strip().split()
        operation = input_lst[0]
        temp_set = set(input().strip().split())

        if operation == 'intersection_update':
            set_.intersection_update(temp_set)
        elif operation == 'update':
            set_.update(temp_set)
        elif operation == 'symmetric_difference_update':
            set_.symmetric_difference_update(temp_set)
        elif operation == 'difference_update':
            set_.difference_update(temp_set)

    print(sum(list(map(int, set_))))
