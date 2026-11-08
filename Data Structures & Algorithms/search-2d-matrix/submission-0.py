class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row = 0
        r_row = len(matrix) - 1
        # find the row
        while l_row <= r_row:
            m_row = (l_row + (r_row - l_row)//2)
            row_start, row_end = matrix[m_row][0], matrix[m_row][-1]
            print(row_start,row_end)
            if target >= row_start and target <= row_end:
                l_inner = 0
                r_inner = len(matrix[m_row]) - 1
                while l_inner <= r_inner:
                    m_inner = (l_inner + (r_inner - l_inner)//2)
                    if target == matrix[m_row][m_inner]:
                        return True
                    elif target < matrix[m_row][m_inner]:
                        r_inner = m_inner - 1
                    elif target > matrix[m_row][m_inner]:
                        l_inner = m_inner + 1
                return False
            elif target < row_start:
                r_row = m_row - 1
            elif target > row_start:
                l_row = m_row + 1
        return False
