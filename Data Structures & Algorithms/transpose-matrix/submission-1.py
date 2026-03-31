class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Model Answer: Iteration -Ⅱ
        rows = len(matrix)
        cols = len(matrix[0])
        
        if rows == cols:
            for r in range(rows):
                for c in range(r):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            return matrix 

        output = [[0]*rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                output[c][r] = matrix[r][c]

        return output       