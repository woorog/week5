import sys

hu,tc=map(int,sys.stdin.readline().split())

reps = list(range(hu+1))

sets = {}
def find(n):
    if reps[n] != n:
        reps[n] = find(reps[n])
    return reps[n]

def union(node1, node2):
    rep1 = find(node1)
    rep2 = find(node2)
    if rep1 != rep2:
        reps[rep2] = rep1

for _ in range(tc):
    P,a,b=map(int,sys.stdin.readline().split())
    if P==1:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a,b)





