import sys
import math

def count5s(N):
    num_5 = 0
    
    for i in range(1, 14): # 5^10은 최대 N보다 크다.
        num_5 += N//(5**i)
    
    
    return num_5

if __name__=="__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        print(count5s(N))