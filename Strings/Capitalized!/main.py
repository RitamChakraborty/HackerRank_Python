# https://www.hackerrank.com/challenges/capitalize/problem


def solve(string):
    output = ""
    lst = string.split(" ")
    for i in lst:
        output += i[:1].upper() + i[1:] + " "

    return output


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
