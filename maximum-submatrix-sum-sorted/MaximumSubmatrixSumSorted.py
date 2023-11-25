'''
Given a row-wise and column-wise sorted matrix. Find the maximum submatrix sum.
ex:
    [
        [-10, -5, -3, 5],
        [-5, 5, 10, 20],
        [-1, 7, 15, 22],
        [4, 10, 17, 30]
    ]
    maxSum = 136
'''

def maximumSubMatrixSumSorted(matrix):
    '''
    Main idea: the solution will contain the bottom rightmost element
    1. Build PS matrix
    2. Iterate through all elements - find the sum of submatrix with that element as top left corner
        and bottom right corener is already set.
    TC: O(N*M)
    SC: O(N*M)
    '''
    # 1. Build PS matrix
    nrows = len(matrix)
    ncols = len(matrix[0])
    prefixSumMatrix = [[0]*ncols for _ in range(nrows)]

    # row wise prefixSum
    for r in range(nrows):
        previousSum = 0
        for c in range(ncols):
            prefixSumMatrix[r][c] += matrix[r][c] + previousSum
            previousSum = prefixSumMatrix[r][c]
    
    # col wise prefixSum
    for c in range(ncols):
        previousSum = 0
        for r in range(nrows):
            prefixSumMatrix[r][c] += previousSum
            previousSum = prefixSumMatrix[r][c]

    maxMatrixSum = 0
    for r in range(nrows):
        for c in range(ncols):
            curSum = prefixSumMatrix[nrows-1][ncols-1]
            if c-1>=0: curSum -= prefixSumMatrix[nrows-1][c-1]
            if r-1>=0: curSum -= prefixSumMatrix[r-1][ncols-1]
            if c-1>=0 and r-1>=0: curSum += prefixSumMatrix[r-1][c-1]
            maxMatrixSum = max(maxMatrixSum, curSum)
    
    return maxMatrixSum

if __name__ == "__main__":
    inputMatrix = [
        [-10, -5, -3, 5],
        [-5, 5, 10, 20],
        [-1, 7, 15, 22],
        [4, 10, 17, 30]
    ]
    print(maximumSubMatrixSumSorted(inputMatrix))