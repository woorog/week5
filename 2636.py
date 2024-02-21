import copy
import sys
from collections import deque

def bfs(board,y1,x1):
    q=deque()
    q.append((0,0))

    while q:
        y,x=q.pop()
        if x>0:
            if board[y][x-1]==0:
                q.append((y,x-1))
                board[y][x-1]=-1
        if x+1<x1:
            if board[y][x+1]==0:
                q.append((y,x+1))
                board[y][x+1]=-1
        if y>0:
            if board[y-1][x]==0:
                q.append((y-1,x))
                board[y-1][x]=-1
        if y+1<y1:
            if board[y+1][x]==0:
                q.append((y+1,x))
                board[y+1][x]=-1


    return board


y,x = list(map(int, sys.stdin.readline().split()))

block=[]

for _ in range(y):
    block.append(list(map(int, sys.stdin.readline().split())))



move=((0,1),(0,-1),(1,0),(-1,0))

cnt=0
counter=0
ans=99999999999999

while 1:
    cnt=0
    for i in range(y):
        for k in range(x):
            if block[i][k]==1:
                cnt+=1

    if cnt<ans and cnt!=0:
        ans=cnt
    if cnt==0:
        break
    bfsblock=bfs(copy.deepcopy(block),y,x)
    nblock=copy.deepcopy(block)

    for i in range(y):
        for k in range(x):
            if block[i][k]==1:
                for a,b in move:
                    if bfsblock[i+a][k+b]==-1:
                        nblock[i][k]=0
                        break
    counter+=1
    block=nblock

print(counter)
print(ans)








