from typing import List
class Solution:
    def exist(self, board:List[str],word:str)->bool:
        r,c=len(board),len(board[0])
        path=set()
        def dfs(row,col,i):
            if i==len(word):
                return True
            if(row<0 or col<0 or row>=r or col>=c or word[i]!=board[row][col] or (row,col) in path):
                return False
            path.add((row,col))
            result=(dfs(row+1,col,i+1) or dfs(row-1,col,i+1) or dfs(row,col+1,i+1) or dfs(row,col-1,i+1))
            return result
        for i in range(r):
            for j in range(c):
                if dfs(i,j,0):
                    return True                
            return False

s=Solution()
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))

