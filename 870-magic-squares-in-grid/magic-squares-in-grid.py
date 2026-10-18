class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        row,col=len(grid),len(grid[0])
        if row<3 or col<3:
            return 0
        count=0
        for i in range(row-2):
            for j in range(col-2):
                if self.isMagic(grid,i,j):
                    count+=1
        return count
    def isMagic(self,grid:list[list[int]],r:int,c:int)->bool:
        if grid[r+1][c+1]!=5:
            return False
        vals=set()
        for i in range(r,r+3):
            for j in range(c,c+3):
                v=grid[i][j]
                if v<1 or v>9 or v in vals:
                    return False
                vals.add(v)
        for i in range(r,r+3):
            if sum(grid[i][j] for j in range(c,c+3))!=15:
                return False
        for j in range(c,c+3):
            if sum(grid[i][j] for i in range(r,r+3))!=15:
                return False
        if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15:
            return False

        if grid[r][c+2]+grid[r+1][c+1]+grid[r+2][c]!=15:
            return False
        return True
            