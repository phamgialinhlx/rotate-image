class Solution:
    def step_corners(self, corners, n):
        # Top Left
        corners[0][0] = corners[0][0] + 1
        corners[0][1] = corners[0][1] + 1
        # Top Right
        corners[1][0] = corners[1][0] + 1
        corners[1][1] = corners[1][1] - 1
        # Bottom Right 
        corners[2][0] = corners[2][0] - 1
        corners[2][1] = corners[2][1] - 1
        # Bottom Left
        corners[3][0] = corners[3][0] - 1
        corners[3][1] = corners[3][1] + 1

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        step = length // 2
        corners = [[0, 0], [0, length - 1], [length - 1, length - 1], [length - 1, 0]]
        pair = [[0, 1], [1, 2], [2, 3], [3, 0]]
        l = length
        for i in range(step):
            x1, y1, x2, y2, x3, y3, x4, y4 = corners[0][0], corners[0][1], corners[1][0], corners[1][1], corners[2][0], corners[2][1], corners[3][0], corners[3][1] 
            for j in range(l - 1):
                matrix[x1][y1], matrix[x2][y2], matrix[x3][y3], matrix[x4][y4] = matrix[x4][y4], matrix[x1][y1], matrix[x2][y2], matrix[x3][y3]
                y1 = y1 + 1
                x2 = x2 + 1
                y3 = y3 - 1
                x4 = x4 - 1
            l = l - 2
            self.step_corners(corners, length - 1)

            