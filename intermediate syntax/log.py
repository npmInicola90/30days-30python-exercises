n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

def divisor(n):
  x = len([i for i in range(1,n+1) if not n % i])
  return x
  