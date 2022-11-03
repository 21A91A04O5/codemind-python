a,b=map(int,input().split())
c=max(a,b)
while True:
    if(c%a==0 and c%b==0):
        print(c)
        break
    else:
        c+=1