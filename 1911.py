import math
import sys

tc,lens=map(int,sys.stdin.readline().split())

waters=[]
for _ in range(tc):
    a,b=map(int,sys.stdin.readline().split())
    waters.append((a,b))

waters.sort()


start,end=waters[0][0],waters[0][1]
sums=0
for i in range(1, tc):
    ns, ne = waters[i][0], waters[i][1]

    # 아래의 로직에서, 널빤지의 사용을 재계산하는 방식에 오류가 있음.
    # 특히, 널빤지가 다음 웅덩이를 덮지 못할 때의 처리가 올바르지 않음.
    temp = (end - start) % lens
    prov = end - temp + lens

    # prov가 ns+1보다 작은 조건은 널빤지가 다음 물웅덩이를 덮지 못하는 경우를 잘못 계산함.
    # 이 부분은 널빤지의 끝 위치와 다음 물웅덩이의 시작 위치를 비교하는 올바른 방식으로 변경되어야 함.
    if prov < ns + 1:
        sums += math.ceil((end - start) / lens)
        start = ns
        end = ne
    # 다음 물웅덩이가 현재 널빤지로 부분적으로 덮일 수 있는 경우에도 처리가 필요함.
    elif ne > end:
        end = ne

sums+= math.ceil((end-start)/lens)

print(sums)

# import math
# import sys
#
# N,L=map(int,sys.stdin.readline().split())
#
# waters=[]
# for _ in range(N):
#     a,b=map(int,sys.stdin.readline().split())
#     waters.append((a,b))
#
# # 웅덩이들을 시작 위치를 기준으로 정렬
# waters.sort()
#
# # 널빤지 필요 개수와 현재 널빤지의 끝 위치 초기화
# block = 0
# c_end = 0
#
# for start, end in waters:
#     if start > c_end:
#         block += math.ceil((end - start) / L)
#         c_end = start + math.ceil((end - start) / L) * L
#     else:
#         if end > c_end:
#             block += math.ceil((end - c_end) / L)
#             c_end = c_end + math.ceil((end - c_end) / L) * L
#
# print(block)
