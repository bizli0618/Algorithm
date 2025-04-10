import sys

if __name__=="__main__":
    N, M = map(int, sys.stdin.readline().split())
    baskets = [0]*N # 바구니~

    for _ in range(M):
        startIdx, endIdx, ballNum = map(int, sys.stdin.readline().split())
        for idx in range(startIdx-1, endIdx):
            baskets[idx] = ballNum
    
    print(" ".join(str(basket) for basket in baskets))