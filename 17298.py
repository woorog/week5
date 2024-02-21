import copy
import sys
from collections import deque


A = list(map(int, sys.stdin.readline().split()))
nge= [-1] * N
stack = [0]


for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        nge[stack.pop()] = A[i]
    stack.append(i)
print(*nge)





