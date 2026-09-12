class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(0,9,3):
            for j in range(0,9,3):

                count=[0]*10
                for k in range(0,3):
                    for l in range(0,3):
                        if (board[i+k][j+l] != '.' and count[int(board[i+k][j+l])]==1):
                            return False
                        elif  board[i+k][j+l] != '.':
                            count[int(board[i+k][j+l])]=1
        
        for i in range(0,9):
            count=[0]*10
            for j in range(0,9):
                if (board[i][j] != '.' and count[int(board[i][j])]==1):
                    return False
                elif board[i][j] != '.':
                    count[int(board[i][j])]+=1
        
        for j in range(0,9):
            count=[0]*10
            for i in range(0,9):
                if (board[i][j] is not '.' and count[int(board[i][j])]==1):
                    return False
                elif board[i][j] != '.':
                    count[int(board[i][j])]+=1
        
        return True
                
        

        