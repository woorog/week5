import sys

hu,tc,money=map(int,sys.stdin.readline().split())

costs=list(map(int,sys.stdin.readline().split()))

reps = list(range(hu))

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
    a,b=map(int,sys.stdin.readline().split())
    union(a-1,b-1)




for i in range(hu):
    rep = find(i)  # i 번째 원소가 속한 집합의 대표 노드를 찾음
    if rep in sets:
        sets[rep].append(i)  # 이미 sets에 대표 노드가 있으면, 해당 집합에 원소 추가
    else:
        sets[rep] = [i]  # 대표 노드가 sets에 없으면, 새 집합으로 추가


ans=0


for i in sets:
    low=100000000
    for k in sets[i]:
        if costs[k]<low:
            low=costs[k]

    ans+=low


if ans<=money:
    print(ans)
else:
    print("Oh no")