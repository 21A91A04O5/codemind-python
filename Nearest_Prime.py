def prime(n):
    if n==1:
        return False
    count=0    
    for i in range(2,(n//2)+1):
        if n%i==0:
            count=1
            break
    if count==0:
        return True
    else:
        return False
        
t=int(input())
for i in range(t):
    n=int(input())
    for i in range(n,9999):
        if prime(i):
            a=i
            break
    for j in range(n-1,0,-1):
        if prime(j):
            b=j
            break
    if abs(n-a)>abs(n-b):
        print(b)
    elif abs(n-a)==abs(n-b):
        print(b)
    else:    
        print(a)
        