#     Fizz Buzz
n=(int(input("enter a number :")))+1

def fizz_buzz(n):  
   for i in range(1,n):
       if i%3==0 and i%5==0:
           print("Fizz","Buzz")
       elif i%3==0:
           print("Fizz")
       elif i%5==0:
           print("Buzz")
       else :
           print(i)
           
           
fizz_buzz(n)    