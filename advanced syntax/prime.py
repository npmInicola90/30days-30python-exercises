def cal():
    numbers = []
    for i in range (99, 1000):
        if str(i) == str(i)[::-1]:
            numbers.append(i)
    return len(numbers)


    print(cal())
