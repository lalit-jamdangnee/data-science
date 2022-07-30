a=int(input("Enter a number"))
def fact(n):
  if n==1 or n==0:
    return 1
  else:
    return n*fact(n-1)
print("The factorial of the number is ",fact(a))
