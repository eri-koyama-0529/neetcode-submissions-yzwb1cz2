class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        # output = [[0] * rows] * cols <-この書き方だと各列が連動してしまう
        output = [[0 for _ in range(rows)] for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                output[c][r] = matrix[r][c]

        return output       