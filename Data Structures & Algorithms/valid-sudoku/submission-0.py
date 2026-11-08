class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        pos = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                sqr = (i//3,j//3)
                if board[i][j] in pos:
                    if i in pos[board[i][j]][0] or j in pos[board[i][j]][1] or sqr in pos[board[i][j]][2]:
                        return False
                    else:
                        pos[board[i][j]][0].append(i)
                        pos[board[i][j]][1].append(j)
                        pos[board[i][j]][2].append(sqr)
                else:
                    pos[board[i][j]] = [[i],[j],[sqr]]
        return True