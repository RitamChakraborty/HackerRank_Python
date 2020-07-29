import re

if __name__ == '__main__':
    _input = input()
    _match = re.match(r"^(M){0,3}(?!M)(C){0,3}[DM]?(C){0,3}(X){0,3}[CL]?(X){0,3}(I){0,3}[XV]?(I){0,3}$", _input)
    print(bool(_match))
