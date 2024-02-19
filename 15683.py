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
nums=len(q)
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


def dfs(board,deep):
    global mins

    if deep==nums:
        # for i in range(y):
        #     print(board[i])

        cnt=0
        for i in range(y):
            for k in range(x):
                if board[i][k]==0:
                    cnt+=1

        if mins>cnt:
            mins=cnt
        return

    cboard=copy.deepcopy(board)
    nx,ny=q[deep][1],q[deep][0]




    if board[ny][nx]==1:
        br=fill_r(copy.deepcopy(board),ny,nx)
        bl=fill_l(copy.deepcopy(board),ny,nx)
        bu=fill_u(copy.deepcopy(board),ny,nx)
        bd=fill_d(copy.deepcopy(board),ny,nx)
        dfs(br,deep+1)
        dfs(bl,deep+1)
        dfs(bu,deep+1)
        dfs(bd,deep+1)

    if board[ny][nx] == 2:
        blr = fill_l(copy.deepcopy(board), ny, nx)
        blr = fill_r(blr, ny, nx)
        bdu = fill_u(copy.deepcopy(board), ny, nx)
        bdu = fill_d(bdu, ny, nx)
        dfs(blr, deep+1)
        dfs(bdu, deep+1)

    if board[ny][nx] == 3:
        for direction in [(fill_u, fill_r), (fill_r, fill_d), (fill_d, fill_l), (fill_l, fill_u)]:
            new_board = copy.deepcopy(board)
            for fill in direction:
                fill(new_board, ny, nx)
            dfs(new_board, deep + 1)

    # CCTV 유형 4 처리
    if board[ny][nx] == 4:
        for direction in [(fill_l, fill_u, fill_r), (fill_u, fill_r, fill_d), (fill_r, fill_d, fill_l), (fill_d, fill_l, fill_u)]:
            new_board = copy.deepcopy(board)
            for fill in direction:
                fill(new_board, ny, nx)
            dfs(new_board, deep + 1)

    # CCTV 유형 5 처리 (기존 로직이 올바르나, 명확성을 위해 재확인)
    if board[ny][nx] == 5:
        new_board = copy.deepcopy(board)
        fill_l(new_board, ny, nx)
        fill_r(new_board, ny, nx)
        fill_u(new_board, ny, nx)
        fill_d(new_board, ny, nx)
        dfs(new_board, deep + 1)



dfs(board,0)
print(mins)
#  틀린 내 코드
# if board[ny][nx]==3:
#     br=fill_r(copy.deepcopy(board),ny,nx)
#     bl=fill_l(copy.deepcopy(board),ny,nx)
#     bu=fill_u(cboard,ny,nx)
#     bd=fill_d(cboard,ny,nx)
#     bur=fill_u(br,ny,nx)
#     bul=fill_u(bl,ny,nx)
#     brd=fill_d(br,ny,nx)
#     bld=fill_d(bl,ny,nx)
#     dfs(bur,deep+1)
#     dfs(bul,deep+1)
#     dfs(brd,deep+1)
#     dfs(bld,deep+1)
#
# if board[ny][nx]==4:
#     br=fill_r(copy.deepcopy(board),ny,nx)
#     bl=fill_l(copy.deepcopy(board),ny,nx)
#     bu=fill_u(cboard,ny,nx)
#     bd=fill_d(cboard,ny,nx)
#     bur=fill_u(copy.deepcopy(br),ny,nx)
#     bul=fill_u(copy.deepcopy(bl),ny,nx)
#     bdl=fill_d(copy.deepcopy(bl),ny,nx)
#     bulr=fill_l(copy.deepcopy(bur),ny,nx)
#     buld=fill_d(copy.deepcopy(bul),ny,nx)
#     burd=fill_d(copy.deepcopy(bur),ny,nx)
#     bdlr=fill_r(copy.deepcopy(bdl),ny,nx)
#     dfs(bulr,deep+1)
#     dfs(buld,deep+1)
#     dfs(burd,deep+1)
#     dfs(bdlr,deep+1)