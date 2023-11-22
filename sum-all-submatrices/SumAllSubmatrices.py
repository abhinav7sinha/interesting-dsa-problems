'''
Problem Statement: Given a 2D Matrix, find the sum of all its submatrices.
Ex. [
    [9, 6], 
    [5,4]
    ]
All of its submatrices are:
[9], [6], [5], [4],
[9, 6], [5,4],
[9, 5], [6,4],
[[9, 6], [5,4]]

totSum = 24 + 24 + 24 + 24 = 96 
'''

def sumAllSubmatrices(matrix):
    '''
    Another example
    [
        [1,2,3],
        [6,4,5]
    ]

    [1], [2], [3], [6], [5], [4]
    [1,2], [2,3], [6,4], [4,5]
    [1,6], [2,4], [3,5]
    [[1,2],[6,4]], [[2,3],[4,5]]
    [1,2,3], [4,5,6]
    [[1,2,3],[4,5,6]]
    1->6
    2->8
    3->6
    6->6
    4->8
    5->6

    How many submatrices does a matrix of size mxn have?

    no. of ways to choose a subarray of rows * no. of ways to choose a subarray of columns

    no. of rows: m -> no. of subarrays of rows = m*(m+1)/2
                                          cols = n*(n+1)/2

    Q: Can you find sum of all subarrays?
    -- contribution technique
        how many subarrays will the ith element be in?
        st can be any index from 0 to i
        en can be any index from i to n-1
        => (i+1)*(n-i)
    
    Q: So, how many elements will the (i,j)th element be in? (mxn) matrix
        (i+1)*(m-i)*(j+1)*(n-j)

        so in a 2*3 matrix
        0,0: 1*2*1*3
        0,1: 2*2*2 = 8

    '''
    '''
    Approach: Think of solving in 1D
        Find all possible subarrays
        Find contribution of each element
    TC: O(m*n)
    SC: O(1)
    '''
    nrows = len(matrix)
    ncols = len(matrix[0])
    ans = 0
    for r in range(nrows):
        for c in range(ncols):
            count = (r+1)*(nrows-r)*(c+1)*(ncols-c)
            ans += matrix[r][c]*count
    return ans

if __name__ == '__main__':
    inputMatrix = [[9,6], [5,4]]
    print(sumAllSubmatrices(inputMatrix))