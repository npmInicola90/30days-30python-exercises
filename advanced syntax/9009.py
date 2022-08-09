def prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    sh = 3 
    while sh * sh <= n:
        if n % sh == 0:
            return False
        sh += 2    
        return true 
        
def cal():
    counter = 0
    number = 2 
    while True:
        if prime(number):
            counter += 1
            if counter == 10001:
                return number
        number += 1


print(cal())