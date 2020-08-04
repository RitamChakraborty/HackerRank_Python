print("\n".join(["Valid" if len(list(filter(lambda x: str(x).isupper(), list(uid)))) >= 2 and len(
    list(filter(lambda x: str(x).isdigit(), list(uid)))) >= 3 and bool(
    all([uid.count(i) == 1 for i in uid])) else "Invalid" for uid in [input() for _ in range(int(input()))]]))
