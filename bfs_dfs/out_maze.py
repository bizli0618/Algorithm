from collections import deque

def bfs(x, y):
    
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        
    

N, M = map(int, input().split())
maze = []

for _ in range(N):
    maze.append(list(map(int,input())))
    
q = deque([(0,0)])
while q:
    i, j = q.popleft()
    bfs(i,j)