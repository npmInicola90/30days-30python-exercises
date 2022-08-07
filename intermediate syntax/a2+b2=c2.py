first_side = float(input("enter the value of the first side angle : "))
second_side = float(input("enter the value of the second side in your triangle : "))
question = input("what side do you want to know the value of : ( a , b , c ) ")
hypotenuse = (first_side**2 + second_side**2)**0.5
first_base = hypotenuse - second_side or second_side - hypotenuse
second_base = hypotenuse - first_side or first_side - hypotenuse
if question == "a":
    print("the value of a is : ", first_base)
elif question == "b":
    print("the value of b is : ", second_base)
elif question == "c":
    print("the value of c is : ", hypotenuse)













