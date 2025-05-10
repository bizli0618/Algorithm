N, M = map(int, input().split())

iced_bucket = []
for _ in range(N):
    iced_bucket.append(list(map(int,input())))


def ice(x, y):
    if x<0 or x >= N or y<0 or y >=M:
        return False
    
    if iced_bucket[x][y] == 0:
        iced_bucket[x][y] = 1
        ice(x-1, y)
        ice(x+1, y)
        ice(x, y-1)
        ice(x, y+1)
        return True

    return False
    
cnt = 0
for i in range(N):
    for j in range(M):
        if ice(i, j)==True:
            cnt+=1


print(cnt)
# DFS - 재귀로 풀자
