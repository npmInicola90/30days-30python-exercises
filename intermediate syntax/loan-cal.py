n = int(input("Enter the borrowing amount: "))
r_n = 5/100
t = int(input("Enter the number of years: "))
m = t * 12
si = n*r_n*t
print("The simple interest is: ", si)
ci = n + si
print("The compound interest is: ", ci)

owed_money = n * (1 + r_n)
year_worth = owed_money / t 
monthly_payment = year_worth / 12
 
print("the amount of money you will totally have to pay is ", owed_money)
print("the amount of money you will have to pay yearly is ", year_worth)
print("the amount of money you will have to pay monthly is ", monthly_payment)

#end of session
