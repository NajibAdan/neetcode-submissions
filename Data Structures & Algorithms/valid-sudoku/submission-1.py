class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_array = [[] for _ in range(9)]
        col_array = [[] for _ in range(9)]
        grid_array = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    grid_pos = (i // 3) * 3 + (j // 3)
                    # check if the current number is already in the row
                    if (
                        board[i][j] in row_array[i]
                        or board[i][j] in col_array[j]
                        or board[i][j] in grid_array[grid_pos]
                    ):
                        # print(f"i:{i}, j:{j}, row_array: {row_array[i]}, num: {board[i][j]}, col_array: {col_array[j]}, grid_pos: {grid_pos}, grid_array: {grid_array[grid_pos]}")
                        return False
                    else:
                        # print(f"i:{i}, j:{j}, row_array: {row_array}, col_array: {col_array}")
                        row_array[i].append(board[i][j])
                        col_array[j].append(board[i][j])
                        grid_array[grid_pos].append(board[i][j])
        return True
