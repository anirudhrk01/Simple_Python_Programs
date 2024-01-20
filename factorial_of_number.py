
n=int(input("enter a number to find its factorial :"))
  
def factorial(n):
     fact=1
     while n>0:
         fact=fact*n
         n-=1
     return fact
 
print(f"factorial of {n} is :",factorial(n))    