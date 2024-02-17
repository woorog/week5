import copy
import sys
from collections import deque

n=int(sys.stdin.readline())

rbg=[[] for _ in range(n)]

for k in range(n):
    for i in map(str,sys.stdin.readline().strip()):
        rbg[k].append(i)

norbg=copy.deepcopy(rbg)

for k in range(n):
    for i in range(n):
        if norbg[k][i]=='R':
            norbg[k][i]='G'

ans1=0
ans2=0

for i in range(n):
    for k in range(n):
        if rbg[i][k]!='N':
            q=deque()
            q.append((i,k,rbg[i][k]))
            rbg[i][k]='N'
            ans1 +=1
            while q:
                y,x,color=q.pop()
                if x+1<n and rbg[y][x+1]!='N' and color==rbg[y][x+1]:
                    q.append((y,x+1,color))
                    rbg[y][x+1]='N'
                if y+1<n and rbg[y+1][x]!='N' and color==rbg[y+1][x]:
                    q.append((y+1,x,color))
                    rbg[y+1][x]='N'
                if x-1>=0 and rbg[y][x-1]!='N' and color==rbg[y][x-1]:
                    q.append((y,x-1,color))
                    rbg[y][x-1]='N'
                if y-1>=0 and rbg[y-1][x]!='N' and color==rbg[y-1][x]:
                    q.append((y-1,x,color))
                    rbg[y-1][x]='N'

for i in range(n):
    for k in range(n):
        if norbg[i][k]!='N':
            q=deque()
            q.append((i,k,norbg[i][k]))
            norbg[i][k]='N'
            ans2 +=1
            while q:
                y,x,color=q.pop()
                if x+1<n and norbg[y][x+1]!='N' and color==norbg[y][x+1]:
                    q.append((y,x+1,color))
                    norbg[y][x+1]='N'
                if y+1<n and norbg[y+1][x]!='N' and color==norbg[y+1][x]:
                    q.append((y+1,x,color))
                    norbg[y+1][x]='N'
                if x-1>=0 and norbg[y][x-1]!='N' and color==norbg[y][x-1]:
                    q.append((y,x-1,color))
                    norbg[y][x-1]='N'
                if y-1>=0 and norbg[y-1][x]!='N' and color==norbg[y-1][x]:
                    q.append((y-1,x,color))
                    norbg[y-1][x]='N'

print(ans1,ans2)