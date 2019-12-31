# https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap


def wrap(input_string, width):
    wrapper = textwrap.TextWrapper(width=width)
    word_list = wrapper.wrap(input_string)
    s = "\n".join(word_list)
    return s


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)