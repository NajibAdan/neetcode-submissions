class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grids = [[set(),set(),set()],
                [set(),set(),set()],
                [set(),set(),set()]]
        row  = [set() for _ in range(9)] 
        col  = [set() for _ in range(9)] 

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                # check if the num exists in row or column
                grid = grids[i//3][j//3]
                if num in row[i] or num in col[j] or num in grid:
                    return False
                row[i].add(num)
                col[j].add(num)
                grids[i//3][j//3].add(num)
        return True
                