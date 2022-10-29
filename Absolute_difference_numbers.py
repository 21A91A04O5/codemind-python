import math
n,m=map(int,input().split())
a=int(math.log10(n)+1)
b=n%math.pow(10,m)
c=n//math.pow(10,a-m)
print(int(abs(b-c)))