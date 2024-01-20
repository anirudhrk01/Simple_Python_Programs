

def sample(n):
    sum=0
    for i in range(n+1):
        sum=sum+i
    return sum    
    
n=int(input("Enter a number "))
print(f"sum of numbers upto {n} is {sample(n)}")    

    