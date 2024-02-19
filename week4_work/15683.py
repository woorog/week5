import copy
import sys
from collections import deque

y,x=map(int,sys.stdin.readline().split())

board=[[0]*x for _ in range(y)]
cctv=[]
q=[]

for i in range(y):
    k=list(map(int,sys.stdin.readline().split()))
    cnt=0
    for l in k:
        board[i][cnt]=l
        if l==1 or l==2 or l==3 or l==4 or l==5:
            q.append((i,cnt))
        cnt+=1

mins=99999999

def fill_l(b, y, x):
    for i in range(x, -1, -1):
        if b[y][i] == 6: break
        if b[y][i] == 0: b[y][i] = -1
    return b

def fill_r(b, y, x):
    for i in range(x, len(b[0])):
        if b[y][i] == 6: break
        if b[y][i] == 0: b[y][i] = -1
    return b
def fill_u(b, y, x):
    for i in range(y, -1, -1):
        if b[i][x] == 6: break
        if b[i][x] == 0: b[i][x] = -1
    return b
def fill_d(b, y, x):
    for i in range(y, len(b)):
        if b[i][x] == 6: break
        if b[i][x] == 0: b[i][x] = -1
    return b

print(q)
def dfs(q,board,deep):
    global mins
    if deep==len(q):
        print(board)
        cnt=0
        for i in range(y):
            for k in range(x):
                if board[i][k]==0:
                    cnt+=1

        if mins>cnt:
            mins=cnt
        return

    cboard=copy.deepcopy(board)
    nq=copy.deepcopy(q)
    nx,ny=q[deep][1],q[deep][0]



    if board[ny][nx]==1:
        br=fill_r(cboard,ny,nx)
        bl=fill_l(cboard,ny,nx)
        bu=fill_u(cboard,ny,nx)
        bd=fill_d(cboard,ny,nx)
        dfs(nq,br,deep+1)
        dfs(nq,bl,deep+1)
        dfs(nq,bu,deep+1)
        dfs(nq,bd,deep+1)

    if board[ny][nx] == 2:
        blr = fill_l(copy.deepcopy(cboard), ny, nx)
        blr = fill_r(blr, ny, nx)
        bdu = fill_u(copy.deepcopy(cboard), ny, nx)
        bdu = fill_d(bdu, ny, nx)
        dfs(nq, blr, deep+1)
        dfs(nq, bdu, deep+1)

    if board[ny][nx]==3:
        br=fill_r(cboard,ny,nx)
        bl=fill_l(cboard,ny,nx)
        bu=fill_u(cboard,ny,nx)
        bd=fill_d(cboard,ny,nx)
        bur=fill_u(br,ny,nx)
        bul=fill_u(bl,ny,nx)
        brd=fill_d(br,ny,nx)
        bld=fill_d(bl,ny,nx)
        dfs(nq,bur,deep+1)
        dfs(nq,bul,deep+1)
        dfs(nq,brd,deep+1)
        dfs(nq,bld,deep+1)

    if board[ny][nx]==4:
        br=fill_r(cboard,ny,nx)
        bl=fill_l(cboard,ny,nx)
        bu=fill_u(cboard,ny,nx)
        bd=fill_d(cboard,ny,nx)
        bur=fill_u(br,ny,nx)
        bul=fill_u(bl,ny,nx)
        bdl=fill_d(bl,ny,nx)
        bulr=fill_l(bur,ny,nx)
        buld=fill_d(bul,ny,nx)
        burd=fill_d(bur,ny,nx)
        bdlr=fill_r(bdl,ny,nx)
        dfs(nq,bulr,deep+1)
        dfs(nq,buld,deep+1)
        dfs(nq,burd,deep+1)
        dfs(nq,bdlr,deep+1)
    if board[ny][nx] == 5:
        bdlru = fill_l(copy.deepcopy(cboard), ny, nx)
        bdlru = fill_r(bdlru, ny, nx)
        bdlru = fill_u(bdlru, ny, nx)
        bdlru = fill_d(bdlru, ny, nx)  # 모든 방향을 한 번에 처리
        dfs(nq, bdlru, deep+1)



dfs(q,board,0)
print(mins)

