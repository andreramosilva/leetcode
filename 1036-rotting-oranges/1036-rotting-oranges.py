class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        minutes = 0

        #search for rotten oranges and fillupp the queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append((i,j,minutes))

        #BFS
        while queue:
                i,j,minutes = queue.popleft()
                for di,dj in directions:
                    ni, nj = i + di, j + dj
                    #Checking if is in the bounderies of the grid and if is a fresh orange
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                        queue.append((ni,nj,minutes+1))
                        grid[i+di][j+dj] = 2
                        
        #looking for a fresh orange
        for r in grid:
            if 1 in r:
                return -1

        return minutes