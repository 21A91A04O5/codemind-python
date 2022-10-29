def reve(n):
    temp=n
    rev=0
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    if temp==rev:
        return True
    else:
        return False
    
n=int(input())  
temp=n
for i in range(n-1,0,-1):
    if(reve(i)==True):
        a=i
        break
n=n+1    
while(n):
    if(reve(n)==True):
        b=n
        break
    n+=1
    
if abs(temp-a)==abs(b-temp): 
    print(a,b)
elif abs(temp-a)<(b-temp):
    print(a)
else:
    print(b)