import math
n=int(input())
a=n*n
b=int(math.log10(n)+1)
c=a%math.pow(10,b)
if(n==c):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")