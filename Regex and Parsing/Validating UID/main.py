# https://www.hackerrank.com/challenges/validating-uid/problem
import re

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        uid = input()
        two_uppercase = "(?=(?:[a-z\d]*[A-Z][a-z\d]*){2,})"
        three_digits = "(?=(?:[a-zA-Z]*\d[a-zA-Z]*){3,})"
        unique_characters = "(?:([a-zA-Z\d])(?!.*\1))"

        match = re.match(
            r"^(?=(?:[a-z\d]*[A-Z][a-z\d]*){2,})(?=(?:[a-zA-Z]*\d[a-zA-Z]*){3,})(?:([a-zA-Z\d])(?!.*\1)){10}$", uid)

        if match:
            print("Valid")
        else:
            print("Invalid")

# One liner
# print("\n".join(["Valid" if len(list(filter(lambda x: str(x).isupper(), list(uid)))) >= 2 and len(
#     list(filter(lambda x: str(x).isdigit(), list(uid)))) >= 3 and bool(
#     all([uid.count(i) == 1 for i in uid])) else "Invalid" for uid in [input() for _ in range(int(input()))]]))
