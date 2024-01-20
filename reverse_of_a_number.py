n=int(input("enter a number to find reverse : "))


def reverse(n):
    reverse_no=0
    
    while n>0:
        mod=n%10
        reverse_no=reverse_no*10+mod
        n=n//10
    return reverse_no    

print("reverse is :",reverse(n))
        