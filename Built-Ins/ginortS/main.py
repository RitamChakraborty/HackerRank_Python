if __name__ == '__main__':
    string = input().strip()
    smalls = [i for i in string if i.islower()]
    capitals = [i for i in string if i.isupper()]
    odd_numbers = [i for i in string if i.isdigit() and int(i) % 2 != 0]
    even_numbers = [i for i in string if i.isdigit() and int(i) % 2 == 0]

    sorted_string = sorted(smalls) + sorted(capitals) + sorted(odd_numbers) + sorted(even_numbers)
    print(*sorted_string, sep="")

# One liner solution
# print(*[sorted([i for i in string if i.islower()]) + sorted([i for i in string if i.isupper()]) + sorted([i for i in string if i.isdigit() and int(i) % 2 != 0]) + sorted([i for i in string if i.isdigit() and int(i) % 2 == 0]) for string in [input()]][0], sep='')
