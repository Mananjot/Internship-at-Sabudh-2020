"""
Question3: Search a 2d Matrix

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example:
Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.

Given target = 20, return false.

"""

def solution(matrix, target):
    if len(matrix) == 0:
        return False
    n = len(matrix[0])  
    m = len(matrix)  
    for i in range(m):                 
        low = 0                                 
        high = n - 1                         
        while low <= high:
            mid_column = (low + high) // 2         
        
            if matrix[i][mid_column] == target:
                return True
            if matrix[i][mid_column] > target:
                high = mid_column - 1
            elif matrix[i][mid_column] < target:
                low = mid_column + 1
    return False

input = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

solution(input, 5)