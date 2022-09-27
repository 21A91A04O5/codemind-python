n=int(input())
sum=0
for i in range(1,n//2+1,1):
    if(n%i==0):
        sum=sum+i
if(n==sum):
    print('True')
else:
    print('False')

        
     