''' 
Design an algorithm that, given a string s of length n, on the alphabet
of the 3 symbols 0, 1 and 2, print all strings of length n on the same alphabet
that differ from X in each position. 
'''
def differStrings(s):

    def help(curr,i,n):
        if i == n:
            print(curr)
            return
        if curr[i] == '0':
            help(curr[:i] + '1' + curr[i + 1:], i+1, n)
            help(curr[:i] + '2' + curr[i + 1:], i+1, n)
        elif curr[i] == '1':
            help(curr[:i] + '0' + curr[i + 1:], i+1, n)
            help(curr[:i] + '2' + curr[i + 1:], i+1, n)
        elif curr[i] == '2':
            help(curr[:i] + '0' + curr[i + 1:], i+1, n)
            help(curr[:i] + '1' + curr[i + 1:], i+1, n)
        
    help(s, 0, len(s))
#Time complexity -> O(n * S(n)) where S(n) is the number of strings to print


'''
Given an integer n, prints all binary strings
long n in which 3 consecutive identical symbols never appear.
'''
def noThreeIdSys(n):

    def help(curr,n):
        if len(curr) == n:
            print(curr)
            return
        if len(curr) < 2 or curr[-1] != '0' or curr[-2] != '0':
            help(curr + '0', n)
        if len(curr) < 2 or curr[-1] != '1' or curr[-2] != '1':
            help(curr + '1', n)
        
    help('', n)
#Time complexity -> O(n * S(n)) where S(n) is the number of strings to print


'''
Given an integer n, print all n*n matrices that have values in {'a', 'b', 'c'} 
with the property that all symbols in each row are all equal.
'''
def matrixEqualRows(n):

    def help(matrix, alfa, i, n):
        if i == n:
            for symb in matrix:
                print([symb]*n)
            print()
            return
        for s in alfa:
            matrix[i] = s
            help(matrix, alfa, i+1, n)

    alfa = ['a', 'b', 'c']
    matrix = [0] * n
    help(matrix, alfa, 0, n)
#Time complexity -> O(n^2 * S(n)) where S(n) is the number of matrix to print


'''
Given n, print all the permutations of the numbers from 1 to n such that 
never appear two adjacent both odd or even numbers
'''
def permutations(n):

    def help(curr, alfa, n, taken):
        if len(curr) == n:
            print(''.join(map(str,curr)))
            return
        if len(curr) == 0:
            for i in alfa:
                if taken[i-1] == 0:
                    taken[i-1] = 1
                    help(curr + [i], alfa, n, taken)
                    taken[i-1] = 0
        elif curr[-1] % 2 == 0:
            for i in alfa:
                if int(i) % 2 == 1:
                    if taken[i-1] == 0:
                        taken[i-1] = 1
                        help(curr + [i], alfa, n, taken)
                        taken[i-1] = 0
        else:
            for i in alfa:
                if i % 2 == 0:
                    if taken[i-1] == 0:
                        taken[i-1] = 1
                        help(curr + [i], alfa, n, taken)
                        taken[i-1] = 0

    mySet = set()
    taken = [0] * (n)
    for i in range(1, n+1):
        mySet.add(i)
    help([], mySet, n, taken)
#Time complexity -> O(n^2 * S(n)) where S(n) is the number of permutations to print


'''
Given n,k integers such that k <= n print all the permutations of the first n integers
in which there are at least k fix points.
A fix point is an item i that appears in the position i of the permutation.
'''
def permutationsFixPoints2(n, k):

    def help(curr, alfa, n, k, taken, fixPoints):
        if len(curr) == n:
            print(curr)
            return
        poxFixPoints = 0
        for i in alfa:
            if taken[int(i)] == 0 and int(i) >= len(curr):
                poxFixPoints += 1
        if fixPoints + poxFixPoints >= k:
            for i in range(n):
                if taken[i] == 0:
                    taken[i] = 1
                    if len(curr) == i:
                            help(curr + alfa[i], alfa, n, k, taken, fixPoints+1)
                    else:
                            help(curr + alfa[i], alfa, n, k, taken, fixPoints)
                    taken[i] = 0
    
    taken = [0] * n
    help('', [str(i) for i in range(n)], n, k, taken, 0)
#Time complexity -> O(n^2 * S(n)) where S(n) is the number of permutations to print


'''
We have a matrix of integers of size n * n. 
A descent on this matrix is a sequence of n matrix cells with the following constraints:
- the cells belong to different rows of the matrix
- the first cell belongs to the first row of the matrix
- every other cell is adjacent (vertically or diagonally) to the cell that it 
precedes
-> Design an algorithm that, given the matrix prints all possible descents by M.
'''
def matrixDescents(matrix):

    def BK(matrix, i, j, n, curr):
        if i != (n - 1):
            BK(matrix, i+1, j, n, curr + [matrix[i+1][j]])
            if j != (n - 1):
                BK(matrix, i+1, j + 1, n, curr + [matrix[i+1][j+1]])
            if j != 0:
                BK(matrix, i+1, j - 1, n, curr + [matrix[i+1][j-1]])
        else:
            print(curr)

    n = len(matrix)
    for j in range(n):
        BK(matrix, 0, j, n, [matrix[0][j]])
    return
#Time complexity -> O(n * S(n)) where S(n) is the number of matrix to print


'''
Given n, print all ternary sequences (0,1,2) in which no adjacent even digits appear
'''
def ternarySeq(n):
    
    def BK(n, i, curr, last):
        if i == n:
            print(curr)
            return 
        for j in range(3):
            if j == 1 or last == 1:
                BK(n, i+1, curr + str(j), j)
    
    BK(n, 0, '', 1)
#Time complexity -> O(n * S(n)) where S(n) is the number of sequences to print


'''
Given n prints all binary n * n square matrices, where the number of 0s 
in each column is less than or equal to the number of 1s in the column.
'''
def matrixLessZeros(n):

    def BK(matrix, i, j, n, count):
        if i == n:
            for row in matrix:
                print(row)
            print()
            return
        if (count[j] + 1) <= (n // 2):
            matrix[i][j] = 0
            count[j] += 1
            if j == (n - 1):
                BK(matrix, i+1, 0, n, count)
            else:
                BK(matrix, i, j+1, n, count)
            count[j] -= 1
        matrix[i][j] = 1
        if j == (n - 1):
            BK(matrix, i+1, 0, n, count)
        else:
            BK(matrix, i, j+1, n, count)

    matrix = [[-1]*(n) for _ in range(n)]
    count = [0] * n
    BK(matrix, 0, 0, n, count)
#Time complexity -> O(n^2 * S(n)) where S(n) is the number of matrix to print


'''
Given n print all the binary strings of length 2*n such that the number of 1s
in the first half is equal to the number of 1s in the second half
'''
def binaryStrings(n):

    def BK(n, i, curr, t1, t2):
        if i == n:
            print(curr)
            return
        empty = n - i
        z1 = n//2 - t1 #number of 0s in the first half
        z2 = n//2 - empty - t2 #number of 0s in the second half
        if i >= n//2:
            #if I have enough 0s
            if z2 + empty - 1 >= z1:
                BK(n, i+1, curr + '1', t1, t2+1)
            #if I have enough 1s
            if t2 + empty - 1 >= t1:
                BK(n, i+1, curr + '0', t1, t2)
        #in the first half I want all the possible combination
        else:
            BK(n, i+1, curr + '0', t1, t2)
            BK(n, i+1, curr + '1', t1+1, t2)
        
    BK(2 * n, 0, '', 0, 0)
#Time complexity -> O(n * S(n)) where S(n) is the number of strings to print


'''
Given n print all the sequences of length n with the alphabet = {'a', 'b', 'c'}
where the symbol 'a' is always followed by two symbols 'b'
'''
def sequencesABC(n):

    def BK(n, i, curr):
        if i == n:
            print(curr)
            return
        if n - i > 2:
            BK(n, i+3, curr + 'abb')
        BK(n, i+1, curr + 'b')
        BK(n, i+1, curr + 'c')

    BK(n, 0, '')
#Time complexity -> O(n * S(n)) where S(n) is the number of strings to print


'''
Given n print all the ternary sequences in which three consecutive
elements never appear such that the sum is an even number
'''
def ternarySeqNoEvenSum(n):

    def BK(i, n, curr):
        if i == n:
            print(curr)
            return
        if i >= 2:
            tot = int(curr[-1]) + int(curr[-2])
            if tot % 2 == 0:
                BK(i+1, n, curr + '1')
            else:
                BK(i+1, n, curr + '0')
                BK(i+1, n, curr + '2')
        else:
            for k in ['0','1','2']:
                BK(i+1, n, curr + k)
    
    BK(0, n, '')
#Time complexity -> O(n * S(n)) where S(n) is the number of sequences to print