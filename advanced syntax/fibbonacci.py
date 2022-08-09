def fibbo():
    total = 0
    c = 0
    y = 1
    while c < 1000000:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total  

print(fibbo())


