import re

n, m = input().split()
scripts = [input() for _ in range(int(n))]
s = ""

for i in range(int(m)):
    for j in scripts:
        s += j[i]

s = re.sub(r"(?<=[a-zA-Z\d])[^a-zA-Z\d]+(?=[a-zA-Z\d])", " ", s)
print(s)
