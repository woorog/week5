import sys

n=int(sys.stdin.readline())

minus=[]
plus=[]

for i in map(int,sys.stdin.readline().split()):
    if i<0:
        minus.append(i)
    else:
        plus.append(i)

minus.sort()
plus.sort()


minnum=0
minusmin=2000000001
plusmin=2000000001
min1=2000000001
min2=2000000001
p1=0
p2=0
m1=0
m2=0


lp=len(plus)
lm=len(minus)
if lp>1:
    p1=plus[0]
    p2=plus[1]
    plusmin=p1+p2
if lm>1:
    m1=minus[lm-1]
    m2=minus[lm-2]
    minusmin=abs(m1+m2)

if lp>0 and lm>0:
    prev=200000001
    for m in minus:
        for p in plus:
            if prev<abs(m+p):
                break
            else:
                if prev>abs(m+p):
                    min1=m
                    min2=p
                prev=abs(m+p)


minnum=abs(min1+min2)

if plusmin<=minnum and plusmin<=minusmin:
    print(p1, p2)  # 여기서는 p1, p2가 이미 오름차순이므로 추가 조건 필요 없음
elif minusmin<=minnum and minusmin<=plusmin:
    print(m2, m1)  # m2, m1을 출력하기 전에 m1, m2 순서가 오름차순인지 확인할 필요 없음, 직접 정렬
else:
    if min1 > min2:  # 이 조건에서 오름차순으로 조정
        min1, min2 = min2, min1
    print(min1, min2)


# print(p1,p2)
# print(m1,m2)
# print(min1,min2)