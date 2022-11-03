a=input()
x=[]
x=a.split(":")
h=int(x[0])
m=int(x[1])
angle=abs(30*h-(11/2)*m)
if angle<360-angle:
    print(angle)
else:
    print(360-angle)