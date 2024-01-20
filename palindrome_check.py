s=str(input("enter a string :"))

def check(s):
     length=len(s)
    
     for i in range(int(length/2)):
        if s[i]!=s[-(i+1)]:
            return "not palindrome"
    
     return "palindrome"
    

print(check(s))   