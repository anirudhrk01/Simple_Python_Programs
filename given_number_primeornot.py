
     

n=int(input("enter number to check if prime :"))

def primeornot(n):
 
 if n<=1:
        return False
    
        
 elif n==2:
           return True

 else:
         flag=0
         val=n
         while n>=2:
            if val%n==0:
                flag+=1
            n-=1
 return flag==1           


print(f"{n} is prime :",primeornot(n))