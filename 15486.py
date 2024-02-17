import sys

num=int(sys.stdin.readline())

costs=[]
for _ in range(num):
    a,b=map(int,sys.stdin.readline().split())
    costs.append([a,b])


dp=[0]*(num+1)

for i in range(num):
    days=costs[i][0]
    cost=costs[i][1]
    if i+days<num+1 and dp[i+days]<dp[i]+cost:
        dp[i+days]=dp[i]+cost
    if dp[i]>dp[i+1]:
        dp[i+1]=dp[i]

print(dp[num])