import math
flag=0
n=int(input())
for i in range(n+1):
    for j in range(n+1):
        if i*i+j*j==n:
            flag=1
            break
        
if flag==0:
    print("False")
else:
    print("True")