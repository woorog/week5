import sys

tc=int(sys.stdin.readline())

stick=[]
sum=0
for i in range(tc):
    a,b=map(int,sys.stdin.readline().split())
    stick.append((a,b))

start,end=stick[0][0],stick[0][1]

for i in range(1,tc):
    a,b=stick[i][0],stick[i][1]
    if a>end:
        sum+=end-start
        start=a
        end=b
    else:
        if end<b:
            end=b

sum+=end-start

print(sum)


