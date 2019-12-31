# https://www.hackerrank.com/challenges/swap-case/problem


def swap_case(input_str):
    string = ""

    for i in list(input_str):
        if i.isupper():
            string += (i.lower())
        else:
            string += (i.upper())

    return string


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
