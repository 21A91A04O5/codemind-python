n=int(input())
e=0
o=0
while(n>0):
    r=n%10
    if(r%2!=0):
        o=1
    elif(r%2==0):
        e=1
    n=n//10    
        
if(o==0):
    print("Even")
elif(e==0):
    print("Odd")
else:
    print("Mixed")