import sys
from collections import deque

if __name__=="__main__":
    std = deque([i for i in range(1,31)])
    
    for _ in range(28):
        id = int(sys.stdin.readline())
        std.remove(id)
    
    for i in std:
        print(i)