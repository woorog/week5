import sys

a=int(sys.stdin.readline())

for i in range(a):

    T_A, T_B, V_A, V_B=map(int,sys.stdin.readline().split())
    D_B_T = T_B * V_B
    S_A_T = T_A * V_A

    end=V_A
    total_time=0
    print(S_A_T)
    if D_B_T < S_A_T:
        a=[0]*S_A_T
        b=[0]*S_A_T

        for i in range(S_A_T):
            a[i]=int(i/T_A)
            if i>D_B_T:
                b[i]=int((i-D_B_T)/T_B)
    else:
        total_time = D_B_T
    print(a)
    print(b)
    print(total_time)
