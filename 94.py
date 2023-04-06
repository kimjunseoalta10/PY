n=int(input())
a=input().split()
t=0
for i in range(n) :
    a[i]=int(a[i])
for i in range(n) :
    for j in range(n-1) :
        if a[j]>a[j+1] :
            a[j]=a[j+1]
for i in range(1) :
    print(a[i])