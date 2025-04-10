import sys

if __name__=="__main__":
    N, x = map(int, sys.stdin.readline().split())
    arr = []
    for _ in range(N+1):
        A, _ = list(map(int, sys.stdin.readline().split()))
        arr.append(A)
    
    res = 0
    for i in range(0, N+1):
        res = (res * x + arr[i]) %(10**9+7)

    print(res)