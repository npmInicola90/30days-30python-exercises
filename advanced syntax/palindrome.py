def palindrone(number):
    if str(number) != str(number)[::-1]:
        return False
    bins = bin(number)[2:]
    return bins == bins[::-1]


def main():
    return list(filter(palindrone, i for i in range(1, 1000)))

print(main())
