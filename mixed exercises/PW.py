import random

def generate_password():
    password = ""
    for i in range(0,10):
        password += chr(random.randint(33,126))
    return password

print(generate_password())
