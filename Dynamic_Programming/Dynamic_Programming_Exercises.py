'''
We have a list of n files of various sizes smaller than C, and a disk of capacity C, 
find an algorithm that calculates the subset of files that can be stored on disk 
and that maximizes the space occupied.
'''
def findSubset1(array, C):
    if not array or C == 0:
        return 0
    leave = findSubset1(array[1:], C)
    if array[0] <= C:
        return leave
    take = findSubset1(array[1:], C - array[0]) + array[0]
    return max(leave, take)
# Time complexity -> O(2^n)


def findSubset2(array, C):
    memo = [[-1]*(C+1) for i in range(len(array) + 1)]

    def helper(array, i, C, memo):
        if memo[i][C] == -1:
            if i == 0 or C == 0:
                memo[i][C] = 0
            else:
                leave, take = helper(array, i-1, C, memo), 0
                if array[i-1] <= C:
                    take = helper(array, i-1, C - array[i-1], memo) + array[i-1]
                memo[i][C] = max(leave, take)
        return memo[i][C]
    
    return helper(array, len(array), C, memo)
# Time complexity -> O(nC)

def findSubset3(array, C):
    n = len(array)
    memo = [[0]*(C + 1) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(C+1):
            if j < array[i-1]:
                memo[i][j] = memo[i-1][j]
            else:
                memo[i][j] = max(memo[i-1][j], memo[i-1][j-array[i-1]] + array[i-1])
    return memo[n][C]
# Time complexity -> O(nC) 