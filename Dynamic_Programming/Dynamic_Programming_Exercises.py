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


'''
We have a backpack with capacity c and n objects, each with a weight p and a value v.
We want to know the maximum value that can be placed in the backpack
'''
def backpack(P, V, c):
    n = len(P)
    T = [ [0] * (c+1) for _ in range(n + 1) ]
    for i in range(1, n+1):
        for j in range(1, c+1):
            if j < P[i - 1]: #I can't insert the object
                T[i][j] = T[i - 1][j]
            else: #I choose the max beetwen if insert or not the object
                T[i][j] = max(T[i - 1][j], V[i - 1] + T[i - 1][j - P[i - 1]])
    return T[n][c]
# Time complexity -> O(n*c)


'''
Give two sequences of symbols X,Y we want to find a subsequence 
common and having maximum length.
'''
def findSubSeq(X,Y):
    n,m = len(X), len(Y)
    T = [ [0] * (m+ 1) for _ in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i] == Y[j]: #longest subsequence without that symbol + 1
                T[i][j] = T[i - 1][j - 1] + 1
            else: #the maximum between the two subsequences
                T[i][j] = max(T[i][j - 1], T[i - 1][j])
    return T[n][m]
# Time complexity -> O(n * m)


'''
Given a positive integer n, count the number of ternary strings long n 
that contain neither substring '02' nor substring '20' 
'''
def ternaryStrings(n):
    #case base is the empty string
    if n == 0:
        return 1
    T = [ [0,0,0] for _ in range(n + 1) ]
    T[0], T[1] = [0,0,0], [1,1,1]
    #IDEA -> a string can termine with:
    # - 0 can append 0 or 1 
    # - 1 can append 0 or 1 or 2
    # - 2 can append 1 or 2
    for i in range(2, n + 1):
        s = sum(T[i - 1])
        T[i][0] = s - T[i - 1][2]
        T[i][1] = s
        T[i][2] = s - T[i - 1][0]
    return sum(T[n])
# Time complexity -> O(n)


'''
Given an integer n, find the number of quaternary strings long n 
that can be obtained by making sure that in strings not two adjacent 
odd digits never appear.
'''
def quaternaryStrings1(n):
    #case base is the empty string
    if n == 0:
        return 1
    T = [ [0,0,0,0] for _ in range(n + 1) ]
    T[0], T[1] = [0,0,0,0], [1,1,1,1]
    #IDEA -> a string can termine with:
    # - even number (0 or 2) and I can append 0 or 1 or 2 or 3     
    # - odd number (1 or 3) and I can append 0 or 2            
    for i in range(2, n + 1):
        even = sum(T[i - 1])
        odd = T[i - 1][0] + T[i - 1][2]
        T[i][0] = T[i][2] = even
        T[i][1] = T[i][3] = odd
    return sum(T[n])
# Time complexity -> O(n)


'''
Given a list A with a range of n coin denominations and an amount k from
achieve find the minimum number of coins needed to get
this amount. If you can't get that amount return -1.
'''
#T[i] -> min number of coins to reach the value i or inf if is impossible
def minCoinsToAmount(A, k):
    T = [float('inf')] * (k + 1)
    for i in range(1, k + 1):
        minVal = float('inf')
        for coin in A:
            val = i - coin
            if val == 0:
                minVal = 1
            elif val > 0:
                if T[val] != float('inf'):
                    minVal = min(minVal, T[val] + 1)
        T[i] = minVal

    if T[k] == float('inf'):
        return -1
    return T[k]
#Time Complexity -> O(n*k)


'''
The display of a mobile phone looks like this:
|1|2|3|
|4|5|6|
|7|8|9|
|*|0|#|
We are looking for a particular telephone number and we know that:
- the number is made up of n digits
- does not contain adjacent identical digits
- when dialing the number on the keypad you only need to move between adjacent keys
horizontally or vertically
-> Design an algorithm that, given n, returns the number of possible combinations 
for the telephone number to search for
'''
def mobilePhone(n):
    #possible move
    memo = {0:[8], 1:[2,4], 2:[1,3,5], 3:[2,6], 4:[1,5,7], 5:[2,4,6,8], 6:[3,5,9], 7:[4,8], 8:[5,7,9,0], 9:[6,8]}
    res = 0
    #for every number which I can start 
    for i in range(10):
        T = [0]*10
        T[i] = 1
        for j in range(2, n+1):
            T1 = [0]*10
            for k in range(10):
                if T[k] != 0:
                    for z in memo[k]:
                        T1[z] += T[k]
            T = T1
        res += sum(T)
    return res
#Time complexity -> O(n)


'''
Given n, return the number of decimal sequences of length n 
in which no adjacent even digits appear
'''
def noEvenDigitsAdjacent(n):
    # set of digits: {0,1,2,3,4,5,6,7,8,9}
    even = odd = 5
    for i in range(2, n + 1):
        # for every sequences of length n-1 I can append every odd number
        # only for the sequences that end with odd number I can append every even number
        even, odd = 5 * odd, 5 * (even + odd)
    return even + odd
#Time complexity -> O(n)


'''
Given n >= 2 we want to count the number of ways in which it is possible to 
obtain n starting from the number 2 and being able to carry out
the only 3 operations of increment by 1, product by 2 and product by 3.
'''
def waysToGetN(n):
    T = [0] * (n + 1)
    T[2] = 1
    for i in range(3, n + 1):
        # We can always add 1 from the sequences that we can reach with n-1
        T[i] += T[i - 1]
        # If n is even we can also multiply by 2 the sequences at n/2
        if i % 2 == 0:
            T[i] += T[i // 2]
        # If n is divisible by 3 we can also multiply by 3 the sequences at n/3
        if i % 3 == 0:
            T[i] += T[i // 3]
    return T[n]
# Time Complexity -> O(n)


'''
Given two integers k, n with 1 <= k <= n find how many different ways
there are to partition the first n positive integers in k subsets
'''
def partitions(n, k):
    T = [ [0]*(n + 1) for _ in range(k + 1) ]
    # base case 0 set with 0 number
    T[0][0] = 1
    # for every number of sets
    for i in range(1, k+1):
        # for every number of integers
        for j in range(1, n+1):
            # we can add the new number at every existing subset
            T[i][j] += i * T[i][j - 1] 
            # we can create a new subset with the new number 
            T[i][j] += T[i - 1][j - 1]
    return T[k][n]