a=int(input("Enter a number"))
def fact(n):
  return n*fact(n-1)
print("The factorial of the number is ",fact(a))
