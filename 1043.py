import sys

hu,tc=map(int,sys.stdin.readline().split())

truep=list(map(int,sys.stdin.readline().split()))
lier=[]

if truep[0]!=0:
    del truep[0]
    for i in truep:

        lier.append(i)

print(lier)



reps = list(range(hu+1))
print(reps)
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

case=[]

for _ in range(tc):
    data=list(map(int,sys.stdin.readline().split()))
    del data[0]
    case.append(data)
    if len(data)>1:
        for i in data:
            print(data[0],i)
            union(data[0],i)

print(case)
print(reps)



for i in range(hu):
    rep = find(i)  # i 번째 원소가 속한 집합의 대표 노드를 찾음
    if rep in sets:
        sets[rep].append(i)  # 이미 sets에 대표 노드가 있으면, 해당 집합에 원소 추가
    else:
        sets[rep] = [i]  # 대표 노드가 sets에 없으면, 새 집합으로 추가

print(sets)
ans=0


#
# for i in sets:
#     low=100000000
#     for k in sets[i]:
#         if costs[k]<low:
#             low=costs[k]
#
#     ans+=low

