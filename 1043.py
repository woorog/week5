import sys
input=sys.stdin.readline
N, M = map(int, input().split())
true_counts = list(map(int, input().split()))
true_people = true_counts[1:]

reps = list(range(N + 1))  # 대표 노드 배열 초기화
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

parties = []

for _ in range(M):
    data = list(map(int, input().split()))[1:]
    parties.append(data)
    for i in range(1, len(data)):
        union(data[0], data[i])


for person in true_people:
    find(person)

cannot_lie = set()
for i, party in enumerate(parties):
    for person in party:
        if find(person) in [find(tp) for tp in true_people]:
            cannot_lie.add(i)
            break
#
# print(cannot_lie)


lie_possible = M - len(cannot_lie)
print(lie_possible)
