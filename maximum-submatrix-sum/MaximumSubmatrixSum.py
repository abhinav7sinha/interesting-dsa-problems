'''
Given a 2D array. Find the maximum submatrix sum.
'''
import math

def maxSubmatrixSum(matrix):
    '''
    1. Build row wise prefix sum array
    2. Now fix le and ri of submatrix
    3. Build a 1D array out of this submatrix
    4. Do kadane's algo
    
    For MxN matrix
    inc. additonal optmization
    TC: O(min((N**2)*M, (M**2)*N))
    SC: O(N*M)
    '''
    nrows = len(matrix)
    ncols = len(matrix[0])

    # 1. Build row wise prefix sum array
    prefSumRows = [[0]*ncols for _ in range(nrows)]
    for r in range(nrows):
        curSum = 0
        for c in range(ncols):
            prefSumRows[r][c] = matrix[r][c] + curSum
            curSum = prefSumRows[r][c]
    for row in prefSumRows:
        print(row)
    # 2. Now fix le and ri of submatrix
    maxSum = -math.inf
    r1, c1, r2, c2 = -1, -1, -1, -1
    for le in range(ncols):
        for ri in range(le, ncols):
            curSum = 0
            st = 0
            for en in range(nrows):
                curVal = prefSumRows[en][ri]
                if le-1>=0:
                    curVal -= prefSumRows[en][le-1]
                curSum += curVal
                if curSum>maxSum:
                    maxSum = curSum
                    r1 = st
                    c1 = le
                    r2 = en
                    c2 = ri

                if curSum < 0:
                    curSum = 0
                    st = en+1
    print((r1,c1), (r2,c2))
    return maxSum




if __name__ == "__main__":
    matrix = [[1, 2, -1, -4, -20],
              [-8, -3, 4, 2, 1],
              [-4, 8, 10, 1, 3],
              [-4, 3, 1, 7, -6]]
    print(maxSubmatrixSum(matrix))