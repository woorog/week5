import sys

a,b=map(int,sys.stdin.readline().split())

pdp=[1]*(a+1)

if b>2:
    for i in range(2,b+1):
        ndp=[0]*(a+1)
        ndp[0]=1
        for k in range(a+1):
            ndp[k]=(pdp[k]+ndp[k-1])%1000000000
        pdp=ndp
    print(ndp[a])
else:
    if b==1:
        print('1')
    else:
        print(a+1)

