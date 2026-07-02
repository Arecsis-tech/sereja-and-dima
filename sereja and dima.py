n=int(input())
c=list(map(int,input().split()))
s=0
d=0
for i in range(n):
    if i==0 or i%2==0:
        if c[0]>c[-1]:
            s=s+c[0]
            c.pop(0)
        else:
            s=s+c[-1]
            c.pop(-1)
    else:
        if c[0]>c[-1]:
            d=d+c[0]
            c.pop(0)
        else:
            d=d+c[-1]
            c.pop(-1)
print(s,d)

