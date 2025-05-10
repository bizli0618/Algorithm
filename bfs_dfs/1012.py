import sys
sys.setrecursionlimit(2500)

def dfs(x, y):
    
    if x<0 or x>=N or y<0 or y>=M:
        return False
    
    if bat[x][y] == 1:
        bat[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        
        return True
    
    return False

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    bat = []
    for _ in range(N):
        tmp = []
        for _ in range(M):
            tmp.append(0)
        bat.append(tmp)

    for _ in range(K):
        X, Y = map(int, input().split())
        bat[Y][X] = 1
    
    
    
    white = 0
    for i in range(N):
        for j in range(M):
            if dfs(i,j) == True:
                white+=1
    print(white)