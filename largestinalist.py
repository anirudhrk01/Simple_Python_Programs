n=int(input("how many elements required in list? : "))

li=[]
i=0
while n!=0:
    i+=1 
    v=int(input(f"val of {i} :"))
    li.append(v)
    n=n-1
    
    
def largestinlist(li):
    largest=0
    for i in li:
        if i>largest:
            largest=i
    return largest

print("largest no is :",largestinlist(li))        


