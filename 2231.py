from collections import deque

def div_sum(N):
    n_str = deque([char for char in str(N)])

    while(n_str):
        N+=int(n_str.popleft())

    return N 

if __name__=="__main__":
    ans = 0
    N = int(input())
    for i in range(1,N-1):
        if div_sum(i)==N:
            ans = i
            break
    print(ans)