'''
Q:  Given an array of size N and Q queries [L,R]
    For all queries, tell if the subarray [L,R] is sorted or not
'''
import math

def subarraySortedQueries(nums, queries):
    '''
    Approach: build a prefixArray which has the count of unsorted pairs
    TC: O(N)
    SC: O(N)
    '''
    prev = -math.inf
    n = len(nums)
    prefUnsortedCount = [0]*n
    curCount = 0

    for i in range(len(nums)):
        if nums[i]<prev:
            curCount += 1
        prefUnsortedCount[i] = curCount
        prev = nums[i]
    
    ans = [False]*len(queries)

    for i, (le, ri) in enumerate(queries):
        if prefUnsortedCount[ri] - prefUnsortedCount[le] == 0:
            ans[i] = True
    
    return ans

if __name__ == '__main__':
    # Test Case 1
    inputNums1 = [1, 2, 3, 5, 4]
    inputQueries1 = [[0, 1], [1, 3], [2, 4]]
    sol1 = subarraySortedQueries(inputNums1, inputQueries1)
    for i, (le, ri) in enumerate(inputQueries1):
        print(inputNums1[le:ri+1], sol1[i])
    print()

    # Test Case 2
    inputNums2 = [1, 2, 3, 5, 4, 7, 6]
    inputQueries2 = [[0, 1], [1, 3], [2, 4], [4, 6], [4,5]]
    sol2 = subarraySortedQueries(inputNums2, inputQueries2)
    for i, (le, ri) in enumerate(inputQueries2):
        print(inputNums2[le:ri+1], sol2[i])