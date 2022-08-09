import random

random.seed(20)

def get_random_number():
    return random.uniform(1, 1),
random uniform(1, 1)    

def unit_circle(point):
    return point[0] ** 2 + point[1] ** 2 > 1

points = [get_random_number() for _ in range(100)]
flagu = [unit_circle(point) for point in points]
print(flagu)
