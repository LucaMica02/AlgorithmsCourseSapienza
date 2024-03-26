""" We have n activities to execute characterized by a pair (start, end) 
and two activities are compatible if they do not overlap.
Return the subset of maximum cardinality """
def maxActivities(activities):
    activities.sort(key = lambda x:x[1])
    currTime = 0
    res = []
    for start, end in activities:
        if start > currTime:
            res.append((start, end))
            currTime = end
    return res
# Time Complexity -> O(nlogn)


""" We have n activities to perform characterized by a pair (start, end) that we
want to perform and we know that the classrooms cannot perform activities in parallel.
Return as few classrooms as necessary """
def minClassroom(activities):
    from heapq import heappop, heappush
    res = [[]]
    heap = [(0,0)]
    activities.sort()
    for start, end in activities:
        free, classroom = heap[0]
        if free < start:
            res[classroom].append((start, end))
            heappop(heap)
            heappush(heap, (end, classroom))
        else:
            res.append([(start, end)])
            heappush(heap, (end, len(res)-1))
    return res
# Time Complexity -> O(nlogn)


""" We have n files of various sizes, which we want to store on a disk 
of capacity k, but we know that the sum of these files exceeds k.
Find a subset of maximum cardinality that can be stored on disk. """
def maxFiles(files, k):
    res = []
    tot, i = 0, 0
    files.sort()
    while tot <= k and i < len(files):
        item = files[i]
        tot += item
        if tot <= k:
            res.append(item)
        i += 1
    return res
# Time Complexity -> O(nlogn)


'''We have two lists A and B, each with 2n elements, we must select n elements 
from A and n elements from B, without selecting elements that occupy the same
index in different lists, such that the sum of the chosen elements is maximum'''
def maxElements(A, B):
    n = len(A)
    res = [None] * n
    diff = [(A[i] - B[i], i) for i in range(n)]
    diff.sort(reverse = True)
    for i in range(n // 2):
        val, ind = diff[i]
        res[ind] = A[ind]
    for i in range(n):
        if not res[i]:
            res[i] = B[i]
    return res
# Time Complexity -> O(nlogn)