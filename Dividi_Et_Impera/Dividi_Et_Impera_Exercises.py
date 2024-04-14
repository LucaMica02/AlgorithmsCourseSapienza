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