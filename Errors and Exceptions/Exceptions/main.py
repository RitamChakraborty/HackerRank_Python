if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        a, b = tuple(input().strip().split())

        try:
            div = int(a) // int(b)
            print(div)
        except ZeroDivisionError as e:
            print("Error Code:", e)
        except ValueError as e:
            print("Error Code:", e)
