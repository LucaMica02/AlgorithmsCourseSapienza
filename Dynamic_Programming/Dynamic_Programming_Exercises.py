'''
We have a list of n files of various sizes smaller than C, and a disk of capacity C, 
find an algorithm that calculates the subset of files that can be stored on disk 
and that maximizes the space occupied
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


'''
Given an integer n we want to count the n-long binary strings in which
no consecutive zeros appear
'''
def countBinaryStrings1(n):
    #T[i] = number of n-long binary strings in which no consecutive zeros appear
    T = [0] * (n + 1)
    if n == 0: return 1
    if n == 1: return 2
    T[0] = 1 #base case (empty string "")
    T[1] = 2 #base case ("0", "1")
    #IDEA T[i]: 
    # the strings to be counted in the T[i-1] in which i can add '1' +
    # the strings to be counted in the T[i-2] in which i can add '10'
    for i in range(2, n+1):
        T[i] = T[i-1] + T[i-2]
    return T[n]
# Time complexity -> O(n) 

'''
Given an integer n we want to count how many binary strings there are
long in which 3 consecutive zeros do not appear
'''
def countBinaryStrings2(n):
    T = [0] * (n+1)
    if n == 0: return 1
    if n == 1: return 2
    if n == 2: return 4
    T[0], T[1], T[2] = 1, 2, 4
    #IDEA T[i]:
    # the strings to be counted in the T[i-1] in which i can add '1' +
    # the strings to be counted in the T[i-2] in which i can add '10' +
    # the strings to be counted in the T[i-3] in which i can add '100'
    for i in range(3, n+1):
        T[i] = T[i-1] + T[i-2] + T[i-3]
    return T[n]


'''
Given an integer n we want to count how many different ways there are of 
accommodate n people in a hotel that has single rooms and double rooms
'''
def accomodatePeople1(n):
    if n == 0 or n == 1:
        return 1
    T = [0] * (n+1)
    T[0] = T[1] = 1
    #IDEA T[i]:
    # T[i-1] ways in which the people i ends up in a single room +
    # T[i-2] * (i-1) ways in which the people i ends up in a double room
    for i in range(2, n+1):
        T[i] = T[i-1] + (i-1) * T[i-2]
    return T[n]
# Time complexity -> O(n)

'''
Given an integer n we want to count how many different ways there are of 
accommodate n people in a hotel that has single rooms and double rooms and triple rooms
'''
def accomodatePeople2(n):
    if n == 0 or n == 1: return 1
    if n == 2: return 2
    T = [0] * (n+1)
    T[0], T[1], T[2] = 1, 1, 2
    for i in range(3,n+1):
        #IDEA T[i]:
        # T[i-1] ways in which the people i ends up in a single room +
        # T[i-2] * (i-1) ways in which the people i ends up in a double room +
        # T[i-3] * gauss summation(i-2) ways in which the people i ends up in a triple room +
        T[i] = T[i-1] + T[i-2] * (i-1) + T[i-3] * (((i-2) * (i-1)) // 2)
    return T[n]
# Time complexity -> O(n)


'''
Given an array A of positive integers we want to calculate the sum
maximum for a subsequence of non-consecutive elements of A
'''
def maxSum1(A):
    n = len(A)
    if n == 0: return 0
    if n == 1: return A[0]
    T = [0] * n
    T[0], T[1] = A[0], max(A[0], A[1])
    #IDEA:
    # I can choose between taking the previous high or the two previous highs + the current item
    for i in range(2, n):
        T[i] = max(T[i-1], T[i-2] + A[i])
    return T[n-1]
# Time complexity -> O(n)

'''
Given an array A of positive integers we want to calculate the sum
maximum for a succession of elements that are at least two apart
'''
def maxSum2(A):
    n = len(A)
    T = [0] * n
    T[0], T[1], T[2] = A[0], max(A[0], A[1]), max(A[0], A[1], A[2])
    #IDEA:
    # I can choose between taking the previous high or the three previous highs + the current item
    for i in range(2, n):
        T[i] = max(T[i-1], T[i-3] + A[i])
    return T[n-1]
# Time complexity -> O(n)