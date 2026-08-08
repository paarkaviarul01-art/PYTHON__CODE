n=int(input("enter a number:"))
if n== 0:
  print("factorial of 0 is 1")
else:
  z=1
  for i in range(1,n+1):
    z=z*i
  print("factorial of " ,n," is ",z)
