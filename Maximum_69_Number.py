n=int(input())
a=n%10
n=n//10
b=n%10
n=n//10
c=n%10
n=n//10
d=n%10
if(d==6):
    d=9
elif(c==6):
    c=9
elif(b==6):
    b=9
elif(a==6):
    a=9
print(d*1000+c*100+b*10+a)    