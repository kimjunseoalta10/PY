n=int(input())
a=input().split()
for i in range(n) :
    a[i]= int(a[i])
d=[]
for i in range(n):
    d.append(0)
for i in range(n):
    d[i]+=a[i]
for i in range(n-1, -1, -1) :
    print(d[i], end=' ')