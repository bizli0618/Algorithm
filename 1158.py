from collections import deque

def joseph(N,K):
    sits = deque([i for i in range(1,N+1)])
    print("<", end="")
    while(sits):
        sits.rotate(-K)
        print(sits.pop(), end="")
        if not sits:
            print(">", end="")
        else:
            print(", ", end="")

if __name__ == "__main__":
    N, K = map(int, input().split())
    joseph(N,K)