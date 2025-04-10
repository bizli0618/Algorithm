import sys

if __name__=="__main__":
    N, M = map(int, sys.stdin.readline().split())
    baskets = [i for i in range(1, N+1)]

    for _ in range(M):
        startIdx, endIdx = map(int, sys.stdin.readline().split())
        tmp = baskets[startIdx-1]
        baskets[startIdx-1] = baskets[endIdx-1]
        baskets[endIdx-1] = tmp

    print(" ".join(str(basket) for basket in baskets))