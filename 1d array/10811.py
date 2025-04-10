import sys

if __name__=="__main__":
    N, M = map(int, sys.stdin.readline().split())

    baskets = [i for i in range(1, N+1)]

    for _ in range(M):
        s, e = map(int, sys.stdin.readline().split())
        startIdx = s-1
        endIdx = e
        
        if (startIdx+1 == endIdx):
            pass
        else:
            tmp = baskets[startIdx:endIdx]
            baskets[startIdx:endIdx] = [tmp[i] for i in range(len(tmp)-1, -1, -1)]

    print(" ".join(str(basket) for basket in baskets))
