import re

if __name__ == '__main__':
    _input = input()
    k = input()
    search = re.search(k, _input)

    if search:
        start = 0
        end = 0

        while search:
            start = search.start() + end
            end += search.end() - 1
            print((start, end))

            if start == end:
                end += 1

            search = re.search(k, _input[end:])
    else:
        print((-1, -1))
