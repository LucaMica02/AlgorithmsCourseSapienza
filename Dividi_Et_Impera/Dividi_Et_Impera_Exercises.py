'''
Given a list of distinct integers, the rank of an element x is the
number of elements that are less than or equal to x in the list.
Given an integer k, with 1 ≤ k ≤ n, we want the element of rank k in the list.
'''
def findRank1(array, k):
    array.sort()
    return array[k - 1]
# Time complexity -> O(nlogn)


'''Idea: divide the array into two parts and see where k will be located'''
from random import randint
def findRank2(array, k):
    if len(array) == 1:
        return array[0]
    pivot = array[randint(0,len(array) - 1)]
    left = [i for i in array if i < pivot]
    right = [i for i in array if i > pivot]
    m = len(left)
    if m >= k:
        return findRank2(left, k)
    elif m == k - 1:
        return pivot
    else:
        return findRank2(right, k - len(left) - 1)
# Time Complexity: 
#   if pivot is the min or the max items:  T(n) = T(n - 1) + O(n) -> O(n^2)
#   if pivot balance fair the list:        T(n) = T(n/2) + O(n) -> O(n)
# Good in the medium case, but bad in the worst case


'''
Idea: if we find a constant c with 0 < c < 1, we can guarantee O(n)
- we divide the list into groups of 5 and find the average of each group
- we will only consider the first n/5 groups obtained
- we find the median between the n/5 groups and use it as a pivot
- this guarantees that max(|left| , |right|) <= 3/4(n)
'''
from math import ceil
def findRank3(array, k):
    n = len(array)
    if n <= 120:
        array.sort()
        return array[k - 1]
    B = [sorted(array[5*i : 5*i + 5])[2] for i in range(n//5)]
    pivot = findRank3(B, ceil(n/10))
    left = [i for i in array if i < pivot]
    right = [i for i in array if i > pivot]
    m = len(left)
    if m >= k:
        return findRank3(left, k)
    elif m == k - 1:
        return pivot
    else:
        return findRank3(right, k - len(left) - 1)
# Time complexity -> T(n) = T(n/5) + T(3/4(n)) + O(n) -> O(n)


'''
Given two integers a,n design an algorithm that compute a^n using only the +,*,// operators
'''
def pow1(a,n):
    res = 1
    for i in range(n):
        res *= a
    return res
# Time complexity -> O(n)

'''
Idea: 
if n is even -> a^n = a^n//2 * a^n//2           [2^10 = 2^5 * 2^5]
if n is odd  -> a^n = a^n//2 * a^n//2 * a       [2^11 = 2^5 * 2^5 * 2]
and so on..
'''
def pow2(a,n):
    if n == 0:
        return 1
    x = pow2(a, n//2)
    if n % 2 == 0:
        return x*x
    return x*x*a
# Time complexity -> O(logn)


'''
Given a binary string S of n bits design an algorithm that calculates 
the number of substrings of S starting with 0 and ending with 1
'''
def findSub1(S):
    res, n = 0, len(S)
    for i in range(n):
        if S[i] == '0':
            curr = '' + S[i]
            for j in range(i + 1, n):
                curr += S[j]
                if curr[-1] == '1':
                    res += 1
    return res
# Time complexity -> O(n^2)

'''
Idea: split the list into two, solve the subproblems and return left solve + right solve + curr
where curr is the number of substrings that start at the left and end at the right
'''
def findSub2(S):
    n = len(S)
    if n <= 1:
        return 0
    n //= 2
    left = findSub2(S[:n])
    right = findSub2(S[n:])
    curr = S[:n].count('0') * S[n:].count('1')
    return left + right + curr
# Time complexity -> T(n) = 2T(n/2) + O(n) =-> O(nlogn)

'''
managing the indexes and the returns i can do the operations in O(1) instead O(n)
'''
def findSub3(S):

    def helper(S, i, j):
        if i == j:
            return [0, S[i].count('0'), S[i].count('1')]
        n = (i + j) // 2
        left = helper(S, i, n)
        right = helper(S, n+1, j)
        curr = left[1] * right[2]
        return [left[0] + right[0] + curr, left[1] + right[1], left[2] + right[2]] 
    
    return helper(S, 0, len(S)-1)[0]
# Time complexity -> T(n) = 2T(n/2) + O(1) =-> O(n)