t=int(input())
for j in range(t):
    n,m=map(int,input().split())
    for i in range(m):
        if (i*i)%m==n:
            print(i)
            break
    else:
        print("-1")